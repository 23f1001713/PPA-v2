from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta


migrate = Migrate()
jwt = JWTManager()
cors = CORS()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portal.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'why i have to store a secret key this is i am goimg to google it '
    app.config['JWT_SECRET_KEY'] = 'this is secret key for my jwt application token generation'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    # Initialize extensions

    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    
    # Register blueprints
    from app.api.auth import auth_bp
    from app.api.admin import admin_bp
    from app.api.student import student_bp
    from app.api.company import company_bp
    from app.api.drive import drive_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    app.register_blueprint(student_bp, url_prefix='/api/student')
    app.register_blueprint(company_bp, url_prefix='/api/company')
    app.register_blueprint(drive_bp, url_prefix='/api/drive')
    
    return app