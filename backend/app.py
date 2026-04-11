from app.scheduler import start_scheduler
from app import create_app
from app.models import db , ceo
app = create_app()
start_scheduler()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        ceo()
    app.run(debug=True)