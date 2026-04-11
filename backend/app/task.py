from app import create_app, mail
from app.celery_worker import make_celery
from flask_mail import Message
import pandas as pd
import os
from app.models import User,Student,Company,Application,PlacementDrives

app = create_app()
celery = make_celery(app)

mail_username = '23f1001713@ds.study.ac.in'




# -----------------------------
# a. DAILY REMINDER JOB
# -----------------------------
@celery.task
def send_daily_reminders():
    with app.app_context():
        students = Student.query.all()

        for s in students:
            user = User.query.filter_by(id = s.user_id).first()
            msg = Message(
                subject="Placement Reminder",
                sender=app.config['MAIL_USERNAME'],
                recipients=[user.email],
                body=f"Hi {s.name}, deadline is Date"
            )
            mail.send(msg)

    return "Daily reminders sent"


# -----------------------------
# b. MONTHLY REPORT
# -----------------------------
@celery.task
def send_monthly_report():
    with app.app_context():
        drives_count = PlacementDrives.query.all()

        applications = Application.query.all()

        applied_count = len(applications)

        selected_count = Application.query.filter_by(status="Selected").count()
        user = User.query.filter_by(role = 'ADMIN').first()
        html = f"""
        <h2>Monthly Placement Report</h2>
        <p><b>Month:</b> </p>
        <ul>
            <li>Drives Conducted: {drives_count}</li>
            <li>Students Applied: {applied_count}</li>
            <li>Students Selected: {selected_count}</li>
        </ul>
        """

        # ✅ Send email
        msg = Message(
            subject="Monthly Placement Report",
            sender=app.config['MAIL_USERNAME'],
            recipients=[user.email],  # admin email
            html=html
        )

        mail.send(msg)

        return "Monthly report sent"


# -----------------------------
# c. CSV EXPORT (ASYNC)
# -----------------------------
@celery.task
def export_csv(student_id):
    with app.app_context():
        student = Student.query.get(student_id)
        apple = Application.query.filter_by(student_id = student.id).all()
        user = User.query.filter_by(id = student.user_id).first()
        data = []
        for a in apple:

            drive = PlacementDrives.query.filter_by(id = a.drive_id).first()
            values = {
            'student_name':student.name,
            'Branch':student.branch,
            'CGPA':student.cgpa,
            'statsu':student.status,
            'Drive_name' : drive.job_title if drive else 'NA',
            'Application status':a.status
        }
            
            data.append(values)
        if not data:
            data.append({
                "message": "No applications found"
        })
        df = pd.DataFrame(data)

        folder = os.path.join(os.getcwd(), "exports")

        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = os.path.join(folder, f"applications_{student_id}.csv")

        df.to_csv(file_path, index=False)

            # Send email after done
        msg = Message(
            subject="CSV Export Ready",
            sender=app.config['MAIL_USERNAME'],
            recipients=[user.email],
            body="Your CSV is ready."
            )
        mail.send(msg)

        return file_path
    # with app.app_context():
    #     data = get_student_applications(student_id)

    #     df = pd.DataFrame(data)

    #     file_path = f"/tmp/applications_{student_id}.csv"
    #     df.to_csv(file_path, index=False)

    #     # Send email after done
    #     msg = Message(
    #         subject="CSV Export Ready",
    #         sender=app.config[mail_username],
    #         recipients=["student@gmail.com"],
    #         body="Your CSV is ready."
    #     )
    #     mail.send(msg)

    # return file_path