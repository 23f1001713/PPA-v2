from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from app.models import User , Company , Student ,PlacementDrives,Application

from app.utils.response import success_response, error_response

drive_bp = Blueprint('drive', __name__)

@drive_bp.route('', methods=['GET'])
@jwt_required()
def get_all_drives():
    """Get all drives with filters"""
    try:
        status = request.args.get('status')
        company_id = request.args.get('company_id')
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        
        query = PlacementDrives.query
        
        if status:
            query = query.filter_by(status=status.upper())
        if company_id:
            query = query.filter_by(company_id=company_id)
        
        drives = query.paginate(page=page, per_page=per_page)
        
        return success_response({
            "drives": [drive.to_dict() for drive in drives.items],
            "total": drives.total,
            "page": page,
            "per_page": per_page,
            "total_pages": drives.pages
        })
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@drive_bp.route('/<int:drive_id>', methods=['GET'])
@jwt_required()
def get_drive_details(drive_id):
    """Get drive details with applications if company/admin"""
    try:
        drive = PlacementDrives.query.get_or_404(drive_id)
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        
        drive_dict = drive.to_dict()
        
        # Add applications if user is company or admin
        if user.role in ['COMPANY', 'ADMIN']:
            applications = Application.query.filter_by(drive_id=drive_id).all()
            drive_dict['applications'] = [app.to_dict() for app in applications]
            
            # For company, add student details
            if user.role == 'COMPANY':
                company = Company.query.filter_by(user_id=user_id).first()
                if drive.company_id == company.id:
                    app_with_students = []
                    for app in applications:
                        student = Student.query.get(app.student_id)
                        app_dict = app.to_dict()
                        app_dict['student'] = student.to_dict() if student else None
                        app_with_students.append(app_dict)
                    drive_dict['applications'] = app_with_students
        
        return success_response(drive_dict)
        
    except Exception as e:
        return error_response(str(e), status_code=500)