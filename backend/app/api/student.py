from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from app.models import User , Company , Student ,PlacementDrives,Application
from app.utils.response import success_response, error_response
from functools import wraps

student_bp = Blueprint('student', __name__)



def get_current_student():
    """Helper to get current student"""
    user_id = get_jwt_identity()
    user  = User.query.filter_by(username = user_id).first()
    return Student.query.filter_by(user_id=user.id).first()

@student_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def student_dashboard():
    """Get student dashboard data"""
    try:
        student = get_current_student()
        if not student:
            return error_response("Student profile not found", status_code=404)
        
        
        total_drives = PlacementDrives.query.filter(PlacementDrives.status == 'APPROVED').count()
        applications = Application.query.filter_by(student_id=student.id).all()
        applied_count = len(applications)
        shortlisted = sum(1 for app in applications if app.status == 'SHORTLISTED')
        selected = sum(1 for app in applications if app.status == 'SELECTED')
        rejected = sum(1 for app in applications if app.status == 'REJECTED')
        user = User.query.get(student.user_id)
        stud = {
                'name':student.name,
                'branch':student.branch,
                'cgpa':student.cgpa,
                'resume':student.resume_path,
                'status':student.status
            }
        
        return success_response({
            "student": stud,
            "user": {
                    "username": user.username,
                    "email": user.email
                },
            "total_drives": total_drives,
            "applied": applied_count,
            "shortlisted": shortlisted,
            "selected": selected,
            "rejected": rejected
            
        })
        
    except Exception as e:
        print(e.message)
        return error_response(str(e), status_code=500)

@student_bp.route('/profile', methods=['GET', 'PUT'])
@jwt_required()
def student_profile():
    """Get or update student profile"""
    try:
        student = get_current_student()
        if not student:
            return error_response("Student profile not found", status_code=404)
        
        if request.method == 'GET':
            user = User.query.get(student.user_id)
            stud = {
                'name':student.name,
                'branch':student.branch,
                'cgpa':student.cgpa,
                'resume':student.resume_path,
                'status':student.status
            }
            return success_response({
                "student": stud,
                "user": {
                    "username": user.username,
                    "email": user.email
                }
            })

        data = request.get_json()
        
        if 'name' in data:
            student.name = data['name']
        if 'branch' in data:
            student.branch = data['branch']
        if 'cgpa' in data:
            student.cgpa = float(data['cgpa'])
        if 'resume_path' in data:
            student.resume_path = data['resume_path']
        db.session.commit()
        return success_response("Profile updated successfully")
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@student_bp.route('/drives', methods=['GET'])
@jwt_required()
def get_drives():
    try:
        student = get_current_student()
        
        # Get all approved drives
        drives = PlacementDrives.query.filter(PlacementDrives.status == 'APPROVED').all()
        
        # Check eligibility and application status for each drive
        drive_list = []
        for drive in drives:
            has_applied = Application.query.filter_by(
                student_id=student.id,
                drive_id=drive.id
            ).first() is not None
            
            # Check eligibility (simplified - implement your logic)
            is_eligible = True  # Implement eligibility check based on CGPA, branch, etc.
            if drive.status == 'APPROVED':
                drive_dict = {
                    'id':drive.id,
                    'title':drive.job_title,
                    'company_name':Company.query.filter_by(id = drive.company_id).first().name,
                    'description':drive.description,
                    'eligibility':drive.eligibility,
                    'deadline':drive.deadline
                }
                drive_dict['has_applied'] = has_applied
                drive_dict['is_eligible'] = is_eligible
                drive_list.append(drive_dict)
        
        return success_response({
            "drives": drive_list,
            "total": len(drive_list)
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@student_bp.route('/drives/apply', methods=['POST'])
@jwt_required()
def apply_for_drive():
    try:

        data = request.json
        drive_id = data.get('id')
        has_applied = data.get('has_applied')
        if has_applied:
            return success_response("Already Registerd for This Drive", status_code=201)
        
        
        student = get_current_student()
        drive = PlacementDrives.query.get_or_404(drive_id)
        
        if drive.status != 'APPROVED':
            return error_response("This drive is not open for applications", status_code=400)
 
        application = Application(
            drive_id=drive_id,
            student_id=student.id
        )
        
        db.session.add(application)
        db.session.commit()
        
        return success_response("Application submitted successfully", status_code=201)
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@student_bp.route('/applications', methods=['GET'])
@jwt_required()
def get_applications():
    """Get student's applications"""
    try:
        student = get_current_student()
        applications = Application.query.filter_by(student_id=student.id).all()
        
        # Get drive details for each application
        app_list = []
        for app in applications:
            drive = PlacementDrives.query.get(app.drive_id)
            app_dict ={
                'id':app.id,
                'student_id':app.student_id,
                'status':app.status,
                'company_id':drive.company_id,
                'job_title':drive.job_title,
                'time':app.time
                }
            # app_dict['drive'] = drive.to_dict() if drive else None
            app_list.append(app_dict)
        
        
        
        
        return success_response({
            "applications": app_list
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@student_bp.route('/history', methods=['GET'])
@jwt_required()
def get_history():
    """Get student's placement history"""
    try:
        student = get_current_student()
        
        # Get all applications with status
        applications = Application.query.filter_by(student_id=student.id).all()
        
        history = []
        for app in applications:
            drive = PlacementDrives.query.get(app.drive_id)
            company = None
            if drive:
                from app.models import Company
                company = Company.query.get(drive.company_id)
            
            history.append({
                "application_id": app.id,
                "drive_title": drive.job_title if drive else "Unknown",
                "company_name": company.company_name if company else "Unknown",
                "application_date": app.application_date.isoformat(),
                "status": app.status,
                "selection_result": app.selection_result
            })
        
        return success_response({
            "history": history,
            "total_applications": len(history)
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@student_bp.route('/export/csv', methods=['POST'])
@jwt_required()
def export_applications_csv():
    try:
        from app.task import export_csv
        student = get_current_student()
        if not student:
            return error_response("Student not found", 404)
        task = export_csv.delay(student.id)

        return success_response({
            "message": "Export started",
            "task_id": task.id
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)