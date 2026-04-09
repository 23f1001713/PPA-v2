from flask import Blueprint, request,jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from app.models import User , Company , Student ,Application
from app.models import PlacementDrives as Drive
from app.utils.response import success_response, error_response
from functools import wraps

admin_bp = Blueprint('admin', __name__)



@admin_bp.route('/dashboard', methods=['GET'])
def admin_dashboard():
    """Get admin dashboard statistics"""
    try:
        t_s = Student.query.count()
        t_c = Company.query.count()
        t_a = Application.query.count()
        t_d = Drive.query.count()
        p_c = Company.query.filter(Company.status !='APPROVED').count()
        p_d = Drive.query.filter_by(status='PENDING').count()
        b_s = Student.query.filter(Student.status != 'APPROVED').count()
        
        
        
        return success_response({
            "statistics": {
                "t_s": t_s,
                "t_c": t_c,
                "t_a": t_a,
                "t_d": t_d,
                "p_c": p_c,
                "p_d": p_d,
                "b_s": b_s
            },
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@admin_bp.route('/companies', methods=['GET'])

def get_companies():
    # Convert companies list to dictionaries
    com_det = Company.query.all()
    total_blocked = Company.query.filter(Company.status != 'APPROVED').all()
    drive = Drive.query.all()

    companies_list = [{
        "id": c.id,
        "name": c.name,
        "status": c.status,
        'drive_count':len([d for d in drive if d.company_id == c.id])
    } for c in com_det]

    # Convert drives list
    

    # Package it for the frontend
    data = {
        "companies": companies_list,
        't_c':len(companies_list),
        't_b':len(total_blocked),
        't_d':len(drive)
    }

    return success_response(data)

@admin_bp.route('/companies/<int:company_id>/approve', methods=['PUT'])

def approve_company(company_id):
    """Approve or reject company registration"""
    try:
        data = request.get_json()
        action = data.get('action')  # 'approve' or 'reject'
        
        company = Company.query.get_or_404(company_id)
        
        if action == 'approve':
            company.approval_status = 'APPROVED'
            message = "Company approved successfully"
        elif action == 'reject':
            company.approval_status = 'REJECTED'
            message = "Company rejected"
        else:
            return error_response("Invalid action. Use 'approve' or 'reject'", status_code=400)
        
        db.session.commit()
        return success_response(company.to_dict(), message)
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@admin_bp.route('/companies/<int:company_id>/blacklist', methods=['PUT'])
@jwt_required()
def blacklist_company(company_id):
    try:
        company = Company.query.get_or_404(company_id)
        if company.status == 'APPROVED':
            company.status ='BLOCKED'
        else:
            company.status = 'APPROVED'
        stat = company.status
        db.session.commit()
        
        return success_response(f"Company {stat} successfully")
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@admin_bp.route('/students', methods=['GET'])
@jwt_required()
def get_students():
    student = Student.query.all()
    s_a = Student.query.filter_by(status = 'APPROVED').all()
    s_b = Student.query.filter(Student.status != 'APPROVED').all()
    apple = Application.query.all()
    student_list = [{
        "id": s.id,
        "name": s.name,
        'branch':s.branch,
        'cgpa':s.cgpa,
        "status": s.status,
        'app_count': len([a for a in apple if apple.student_id == s.id])
    } for s in student]

    data = {
        "students": student_list,
        's_a':len(s_a),
        's_b':len(s_b),
        't_s':len(student)
    }

    return success_response(data)


@admin_bp.route('/students/<int:student_id>/blacklist', methods=['PUT'])
@jwt_required()
def blacklist_student(student_id):
    try:
        student = Student.query.get_or_404(student_id)
        if student.status == 'APPROVED':
            student.status = 'BLOCKED'
        else:
            student.status = 'APPROVED'
        
        sta = student.status
        db.session.commit()
        
        return success_response(f"Student {sta} successfully")
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@admin_bp.route('/drives', methods=['GET'])

def get_drives():
    """Get all drives with filters"""
    
    d = Drive.query.all()
    t_p = len(Drive.query.filter_by(status = 'PENDING').all())
    t_a = len(Drive.query.filter_by(status = 'APPROVED').all())
    t_c = len(Drive.query.filter_by(status = 'CLOSED').all())

    drive_list = [{
        "id": s.id,
        "job_title": s.job_title,
        'eligibility':s.eligibility,
        'description':s.description,
        "status": s.status,
        'deadline':s.deadline
    } for s in d]


    return success_response({
            "drives": drive_list,
            "t_p": t_p,
            "t_a": t_a,
            "t_c": t_c,
            'total':len(d)
            
    })
    

@admin_bp.route('/drives/<int:drive_id>/approve', methods=['PUT'])

def approve_drive(drive_id):
    """Approve or reject placement drive"""
    try:
        data = request.get_json()
        action = data.get('action')  # 'approve' or 'reject'
        
        drive = Drive.query.get_or_404(drive_id)
        
        if action == 'approve':
            drive.status = 'APPROVED'
            message = "Drive approved successfully"
        elif action == 'reject':
            drive.status = 'REJECTED'
            message = "Drive rejected"
        else:
            return error_response("Invalid action. Use 'approve' or 'reject'", status_code=400)
        
        db.session.commit()
        return success_response(drive.to_dict(), message)
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@admin_bp.route('/drives/<int:drive_id>/close', methods=['PUT'])

def close_drive(drive_id):
    """Close a placement drive"""
    try:
        drive = Drive.query.get_or_404(drive_id)
        drive.status = 'CLOSED'
        db.session.commit()
        
        return success_response(drive.to_dict(), "Drive closed successfully")
        
    except Exception as e:
        db.session.rollback()
        return error_response(str(e), status_code=500)

@admin_bp.route('/applications', methods=['GET'])

def get_applications():
    """Get all applications with statistics"""
    try:
        applications = Application.query.all()
        
        stats = {
            "total": len(applications),
            "pending": Application.query.filter_by(status='PENDING').count(),
            "shortlisted": Application.query.filter_by(status='SHORTLISTED').count(),
            "selected": Application.query.filter_by(status='SELECTED').count(),
            "rejected": Application.query.filter_by(status='REJECTED').count(),
            "applications": [app.to_dict() for app in applications]
        }
        
        return success_response(
            stats
        )
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@admin_bp.route('/search', methods=['GET'])

def search():
    """Search companies and students"""
    try:
        query = request.args.get('q', '')
        search_type = request.args.get('type')  # 'company', 'student', or None for both
        
        results = {}
        
        if not search_type or search_type == 'company':
            companies = Company.query.filter(
                Company.company_name.contains(query)
            ).limit(20).all()
            results['companies'] = [comp.to_dict() for comp in companies]
        
        if not search_type or search_type == 'student':
            students = Student.query.filter(
                Student.name.contains(query)
            ).limit(20).all()
            results['students'] = [student.to_dict() for student in students]
        
        return success_response(results, "Search completed")
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@admin_bp.route('/reports/monthly', methods=['GET'])

def monthly_report():
    """Generate monthly report"""
    from datetime import datetime, timedelta
    try:
        # Get current month's data
        now = datetime.now()
        start_of_month = datetime(now.year, now.month, 1)
        
        drives_this_month = Drive.query.filter(Drive.created_at >= start_of_month).count()
        applications_this_month = Application.query.filter(Application.application_date >= start_of_month).count()
        selected_this_month = Application.query.filter(
            Application.application_date >= start_of_month,
            Application.status == 'SELECTED'
        ).count()
        
        return success_response({
            "month": now.strftime("%B %Y"),
            "drives_conducted": drives_this_month,
            "applications_received": applications_this_month,
            "students_selected": selected_this_month,
            "selection_rate": round((selected_this_month / applications_this_month * 100) if applications_this_month > 0 else 0, 2)
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)