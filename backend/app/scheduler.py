from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.task import send_daily_reminders, send_monthly_report

scheduler = BackgroundScheduler()

def start_scheduler():
    # Daily job
    scheduler.add_job(
        func=send_daily_reminders.delay,
        trigger="cron",
        hour=11,
        minute=5
    )

    # Monthly job (1st day)
    scheduler.add_job(
        func=send_monthly_report.delay,
        trigger="cron",
        day=10,
        hour=11,
        minute=8
    )

    scheduler.start()