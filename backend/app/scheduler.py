from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.task import send_daily_reminders, send_monthly_report

scheduler = BackgroundScheduler()

def start_scheduler():
    # Daily job
    scheduler.add_job(
        func=send_daily_reminders.delay,
        trigger="cron",
        hour=8,
        minute=25
    )

    # Monthly job (1st day)
    scheduler.add_job(
        func=send_monthly_report.delay,
        trigger="cron",
        day=12,
        hour=8,
        minute=24
    )

    scheduler.start()