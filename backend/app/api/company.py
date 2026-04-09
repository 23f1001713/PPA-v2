from flask import Blueprint, request,abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from app.models import User , Company , Student ,PlacementDrives,Application
from app.utils.response import success_response, error_response
from datetime import datetime
from functools import wraps

company_bp = Blueprint('company', __name__)




@company_bp.route('/test', methods=['GET'])
def test():
    return success_response({'message':'hello world'})


def get_current_company():
    user_id = get_jwt_identity()
    user = User.query.filter_by(username=user_id).first()
    print(user.email)
    if not user:
        # Returns a 404 instead of crashing with a 500
        abort(404, description="User not found in database") 

    company = Company.query.filter_by(user_id=user.id).first()
    print(company.name)
    if not company:
        abort(404, description="Company not found for this user")

    return company
@company_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def company_dashboard():
    """Get company dashboard data"""
    try:
        company = get_current_company()
        if not company:
            return error_response("Company profile not found", status_code=404)
        drives = PlacementDrives.query.filter_by(company_id=company.id).all()
        applications = db.session.query(Application).join(PlacementDrives).filter(
            PlacementDrives.company_id == company.id
        ).all()
        stats = {
            "total_drives": len(drives),
            "pending_drives": sum(1 for d in drives if d.status == 'PENDING'),
            "approved_drives": sum(1 for d in drives if d.status == 'APPROVED'),
            "closed_drives": sum(1 for d in drives if d.status == 'CLOSED'),
            "total_applications": len(applications),
            "shortlisted": sum(1 for a in applications if a.status == 'SHORTLISTED'),
            "selected": sum(1 for a in applications if a.status == 'SELECTED'),
            "rejected": sum(1 for a in applications if a.status == 'REJECTED')
        }
        
        drives_list = [{
        "id": d.id,
        "title": d.job_title,
        "date": str(d.deadline) if d.deadline else None,
        "status": d.status
    } for d in drives]
        com = {
            'id':company.id,
            'name':company.name,
            'hr':company.hr_contact,
            'website':company.website,
            'status':company.status
        }

        return success_response({
            "company": com,
            "statistics": stats,
            "recent_drives": drives_list
        })
        
    except Exception as e:
        print(e)
        return error_response(str(e), status_code=500)





@company_bp.route('/drives', methods=['GET', 'POST'])
@jwt_required()
def manage_drives():
    """Get all drives or create new drive"""
    try:
        company = get_current_company()
        print(company.name)
        
        if request.method == 'GET':
            drives = PlacementDrives.query.filter_by(company_id=company.id).all()
            drives_list = [{
                "id": d.id,
                "title": d.job_title,
                "date": d.deadline if d.deadline else None,
                "status": d.status,
                'description':d.description
            } for d in drives]

            return success_response({
                "drives": drives_list,
                "total": len(drives)
            })
        
        # POST - Create new drive
        data = request.get_json()
        
        print(data)
        
        
        
        new_drive = PlacementDrives(
            company_id=company.id,
            job_title=data['job_title'],
            description=data['description'],
            eligibility=data['eligibility'],
            deadline=data['deadline']
        )
        
        db.session.add(new_drive)
        db.session.commit()
        
        return success_response("Drive created successfully. ", status_code=200)
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)
    

@company_bp.route('/drives/<int:drive_id>/close', methods=['PUT'])
@jwt_required()
def close_drive(drive_id):
    try:
        # Use get_or_404 to handle missing IDs automatically
        drive = PlacementDrives.query.get_or_404(drive_id)
        
        # IMPROVED LOGIC: Explicitly toggle based on 'CLOSED'
        if drive.status == 'CLOSED':
            drive.status = 'APPROVED' # Or 'PENDING', depending on your flow
        else:
            drive.status = 'CLOSED'
            
        db.session.commit()
        
        # It's best practice to return the new status so the frontend knows what happened
        return success_response({
            "message": f"Drive is now {drive.status}",
            "new_status": drive.status
        })
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)



@company_bp.route('/drives/<int:drive_id>', methods=['GET', 'PUT', 'DELETE'])

def drive_detail(drive_id):
    """Get, update or delete a specific drive"""
    try:
        company = get_current_company()
        drive = PlacementDrives.query.get_or_404(drive_id)
        
        # Check ownership
        if drive.company_id != company.id:
            return error_response("You don't have permission to access this drive", status_code=403)
        
        if request.method == 'GET':
            return success_response(drive.to_dict())
        
        if request.method == 'PUT':
            data = request.get_json()
            
            if 'job_title' in data:
                drive.job_title = data['job_title']
            if 'job_description' in data:
                drive.description = data['job_description']
            if 'eligibility' in data:
                drive.eligibility = data['eligibility']
            if 'deadline' in data:
                drive.deadline = datetime.fromisoformat(data['deadline'].replace('Z', '+00:00'))
            
            db.session.commit()
            return success_response(drive.to_dict(), "Drive updated successfully")
        
        if request.method == 'DELETE':
            db.session.delete(drive)
            db.session.commit()
            return success_response(message="Drive deleted successfully")
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@company_bp.route('/applications', methods=['GET'])
@jwt_required()
def get_applications():
    """Get all applications for company's drives"""
    try:
        company = get_current_company()
        
        # Get all applications for company's drives
        applications = db.session.query(Application).join(PlacementDrives).filter(
            PlacementDrives.company_id == company.id
        ).all()
        
        # Enrich with student and drive details
        app_list = []
        for app in applications:
            student = Student.query.get(app.student_id)
            drive = PlacementDrives.query.get(app.drive_id)
            stu = {
                'name':student.name,
                'branch':student.branch,
                'cgpa':student.cgpa
            }
            driv = {
                'title':drive.job_title,
                'eligibility':drive.eligibility,
                'deadline':drive.deadline,
                'max_a':drive.max_application
            }
            app_list.append({
                "application_id": app.id,
                "student": stu,
                "drive": driv,
                "status": app.status,
                "application_date": app.time
            })
        
        # Statistics
        stats = {
            "total": len(app_list),
            "pending": sum(1 for a in app_list if a['status'] == 'PENDING'),
            "shortlisted": sum(1 for a in app_list if a['status'] == 'SHORTLISTED'),
            "selected": sum(1 for a in app_list if a['status'] == 'SELECTED'),
            "rejected": sum(1 for a in app_list if a['status'] == 'REJECTED')
        }
        
        return success_response({
            "statistics": stats,
            "applications": app_list
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@company_bp.route('/applications/<int:application_id>/status', methods=['PUT'])

def update_application_status(application_id):
    """Update application status (shortlist, select, reject)"""
    try:
        company = get_current_company()
        application = Application.query.get_or_404(application_id)
        
        # Verify ownership through drive
        drive = PlacementDrives.query.get(application.drive_id)
        if drive.company_id != company.id:
            return error_response("You don't have permission to update this application", status_code=403)
        
        data = request.get_json()
        new_status = data.get('status', '').upper()
        
        valid_statuses = ['SHORTLISTED', 'SELECTED', 'REJECTED', 'PENDING']
        if new_status not in valid_statuses:
            return error_response(f"Invalid status. Must be one of: {', '.join(valid_statuses)}", status_code=400)
        
        application.status = new_status
        
        if 'interview_schedule' in data:
            application.interview_schedule = data['interview_schedule']
        if 'selection_result' in data:
            application.selection_result = data['selection_result']
        
        db.session.commit()
        
        return success_response(application.to_dict(), f"Application {new_status.lower()} successfully")
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)