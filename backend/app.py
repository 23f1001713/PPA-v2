from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash , generate_password_hash
from models import db , Student,User,Company,Application,PlacementDrives,ceo
from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_jwt_extended import JWTManager , create_access_token

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
app.config['SECRET_KEY'] = 'why i need to set a secret key'
app.config["JWT_SECRET_KEY"] = "VerySecretKey" # Change this!
jwt = JWTManager(app)
db.init_app(app)

@app.route('/api/register' , methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        response = request.get_json()

        username = response['username']
        email = response['email']
        password = response['password']
        role = response['role']

        user = User.query.filter_by(username=username).first()
        if user:
            return jsonify({'message': 'username already registered'}), 409 
        user = User.query.filter_by(email = email).first()
        if user:
            return jsonify({'message': 'Email already registered'}), 409
        
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
            return jsonify({'message': 'Registration successful. Await admin approval if company.'}),201
       
       
       
       
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
    

@app.route('/api/login' , methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        password = data['password']
        print(username)

        user = User.query.filter_by(username = username).first()
        if user and check_password_hash(user.password, password):
            access_token = create_access_token(identity=username, additional_claims={"role": user.role})
            return jsonify({
                'message': 'Login successful',
                'token': access_token,
                'role': user.role  # Send role so frontend knows where to redirect
            }), 200
        

    return jsonify({'message':'invalid credentials'}),404









if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        ceo()
    app.run(debug = True)
    