import smtplib
from typing import Dict, List

from django.conf import settings

from celery import shared_task
from lib.send_mail import EmailManager


@shared_task(
    bind=True,
    autoretry_for=(smtplib.SMTPException,),
    retry_kwargs={
        "max_retries": settings.CELERY_MAX_RETRY,
        "countdown": settings.CELERY_RETRY_DELAY,
    },
)
def send_email_async( template=None, subject=None, recipients=None, context=None):
    mail = EmailManager(
        template=template, 
        subject=subject, 
        recipients=recipients,
        context=context
    )
    mail.send()
    
