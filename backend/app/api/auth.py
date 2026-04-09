from flask import Blueprint, request,jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db
from app.models import User , Company , Student ,PlacementDrives,Application
from app.utils.response import success_response, error_response

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        password = data['password']
        print(username)

        user = User.query.filter_by(username = username).first()
        if not user:
            return jsonify({'message':'Invalid Username'}),404
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=username, additional_claims={"role": user.role})
            return jsonify({
                'message': 'Login successful',
                'token': access_token,
                'role': user.role  # Send role so frontend knows where to redirect
            }), 200
        return jsonify({'message':'Invalid Password'}),404
        

    return jsonify({'message':'invalid credentials'}),404



@auth_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        response = request.get_json()

        username = response['username']
        email = response['email']
        password = response['password']
        role = response['role']

        user = User.query.filter_by(username=username).first()
        if user:
            print('user already exist')
            return error_response(
                f"Username '{response['username']}' is already taken. Please choose a different username.",
                status_code=409,
                errors=[{"field": "username", "message": "Username already exists"}]
            )
        user = User.query.filter_by(email = email).first()
        if user:
            print('email already exists')
            return error_response(
                f"Email '{response['email']}' is already registered. Please use a different email or login.",
                status_code=409,
                errors=[{"field": "email", "message": "Email already registered"}]
            )
        if role == 'company':
            website = response['website']
            hr = response['hr_contact']
            name = response['company_name']

            new_user = User(
            email = email,
            username = username,
            password = generate_password_hash(password),
            role = 'COMPANY'
            )
            db.session.add(new_user)
            db.session.flush()

            new_company = Company(
                user_id = new_user.id,
                name = name,
                hr_contact = hr,
                website =website
            )

            db.session.add(new_company)
            db.session.commit()
            return jsonify({'message': 'Registration successful. Await admin approval if company.'}),200
       
       
       
       
        if role == 'student':
            name = response['name']
            cgpa = response['cgpa']
            branch = response['branch']
            resume_path = response['path']

            new_user = User(
            email = email,
            username = username,
            password = generate_password_hash(password),
            role = 'STUDENT'
            )
            db.session.add(new_user)
            db.session.flush()

            new_student = Student(
                user_id = new_user.id,
                name = name,
                cgpa = cgpa,
                branch =branch,
                resume_path = resume_path
                )

            db.session.add(new_student)
            db.session.commit()

            return jsonify({'message':'Registration Successful'}),200


        return jsonify({'message': 'Registration successful. Await admin approval if company.'}),201


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():
    """Refresh access token"""
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return error_response("User not found", status_code=404)
        
        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"role": user.role}
        )
        
        return success_response({
            "access_token": access_token
        }, "Token refreshed successfully")
        
    except Exception as e:
        return error_response(str(e), status_code=500)

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    """Logout user (client should discard token)"""
    return success_response(message="Logout successful")