from workers import celery
from datetime import datetime
from flask import current_app as app
from celery.schedules import crontab

# print("crontab ", crontab)

from models import User, Category, db

MINUTES = 60
HOURS = 60 * 60
DAYS = 24 * HOURS
MONTHS = 30 * DAYS


@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="*/2"), print_current_time_job.s(), name="test periodic job"
    )


# @celery_app.task
# def send_reminder_mail():
#     msg = Message("Hello from Flask", recipients=["mailkarankp@gmail.com"])
#     msg.body = "This is a test email sent from a Flask app!"
#     with app.app_context():
#         mail = Mail(app)

#     mail.send(msg)

#     return "Email sent successfully!"


@celery.task()
def just_say_hello(name):
    print("INSIDE TASK")
    result = f"hello, {name}"
    print(result)
    return result


@celery.task()
def print_current_time_job():
    print("START")
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    print("COMPLETE")
