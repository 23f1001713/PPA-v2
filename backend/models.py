from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key = True,nullable = False)
    username = db.Column(db.String(20) , nullable = False , unique = True)
    password = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(60),nullable = False , unique=True)
    role = db.Column(db.String(10),nullable = False) # ADMIN , STUDENT , COMPANY

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    name = db.Column(db.String(30) , nullable = False)
    branch = db.Column(db.String(20) , nullable = False)
    cgpa = db.Column(db.Integer , nullable = False)
    resume_path = db.Column(db.String(100) , nullable = False)
    status = db.Column(db.String(20) ,default = 'APPROVED') # APPROVED , PENDING BLOCKED

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    name = db.Column(db.String(30) , nullable = False)
    hr_contact = db.Column(db.Integer , nullable = False)
    website = db.Column(db.String(100) , nullable = False)
    status = db.Column(db.String(20) ,default = 'APPROVED') # APPROVED , PENDING BLOCKED

class PlacementDrives(db.Model):
    __tablename__ = 'drives'
    id = db.Column(db.Integer , primary_key = True)
    company_id = db.Column(db.Integer , db.ForeignKey('companies.id'))
    job_title = db.Column(db.String(60) , nullable = False )
    description = db.Column(db.String(120),nullable = False)
    eligibility = db.Column(db.String(60) , nullable = False)
    deadline = db.Column(db.String(50) , nullable = False)
    status = db.Column(db.String(20),nullable = False , default = 'APPROVED') # APPROVED,PENDING , REJECTED , CLOSED
    max_applications = db.Column(db.Integer , nullable = False)

class Application(db.Model):
    __tablename__ = 'applications'
    id = db.Column(db.Integer ,primary_key = True)
    student_id = db.Column(db.Integer , db.ForeignKey('students.id'))
    drive_id = db.Column(db.Integer , db.ForeignKey('drives.id'))
    time = db.Column(db.String(30) , default = datetime.now)
    status = db.Column(db.String(30) , default = 'APPLIED') #APPLIED,SHORTLISTED , REJECTED , SELECTED



def ceo():
    admin = User.query.filter_by(role = 'ADMIN').first()

    if not admin:
        new_admin = User(
            username = 'admin',
            password = generate_password_hash('admin123'),
            role = 'ADMIN',
            email = 'admin@gmail.com'
        )
        db.session.add(new_admin)
        db.session.commit()