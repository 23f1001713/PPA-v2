from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
from flask import Flask
from flask_caching import Cache
from flask_mail import Mail
from app.models import db



migrate = Migrate()
jwt = JWTManager()
cors = CORS()
cache = Cache()
mail = Mail()

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

    app.config.update(
        SECRET_KEY="secret again why.....",
        broken_url="redis://localhost:6379/0",
        result_backend="redis://localhost:6379/0",

        CACHE_TYPE="RedisCache",
        CACHE_REDIS_URL="redis://localhost:6379/1",
        CACHE_DEFAULT_TIMEOUT=300,

        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=587,
        MAIL_USE_TLS=True,
        MAIL_USERNAME='23f1001713@ds.study.iitm.ac.in',
        MAIL_PASSWORD="jbzbzwwdqwkkbzuh"
    )
    
    
    # Initialize extensions

    jwt.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    cache.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    
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