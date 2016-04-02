from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from datetime import datetime
# from django.db.models import F

from .models import Payment
from django.core.mail import send_mail


logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/15')),
    name="Check payments status",
    ignore_result=True
)
def check_payments_dates():
    today_min = datetime.combine(datetime.now(), datetime.time.min)
    payments = ( Payment
                .objects
                .filter(
                    status='ONT',
                    dateExpiration__lt =  today_min
                )
        )
    for payment in payments:
        subject = 'Subject'
        message = 'Message'
        from_email = 'hi@arlefreak.com'
        to_email = 'arlefreak@gmail.com'
        payment.status = 'LAT'
        payment.save()
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
            fail_silently=False
        )


@shared_task
def send_notification(body):
    return send_notification(body)
