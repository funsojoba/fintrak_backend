import smtplib
from typing import Dict, List

from django.conf import settings

from celery import shared_task
from lib.send_mail import EmailManager

from django.core.mail import EmailMessage, EmailMultiAlternatives


@shared_task(
    bind=True,
    autoretry_for=(smtplib.SMTPException,),
    retry_kwargs={
        "max_retries": settings.CELERY_MAX_RETRY,
        "countdown": settings.CELERY_RETRY_DELAY,
    },
)
def send_email_async(self, template=None, subject=None, recipients=None, context=None):
    mail = EmailManager(
        template=template, 
        subject=subject, 
        recipients=recipients,
        context=context
    )
    mail.send()
    
@shared_task(
    bind=True,
    autoretry_for=(smtplib.SMTPException,),
    retry_kwargs={
        "max_retries": settings.CELERY_MAX_RETRY,
        "countdown": settings.CELERY_RETRY_DELAY,
    },
)
def send_mail_async(self, template, subject, recipients, context):
    from_email = settings.EMAIL_FROM
    html_content = render_to_string(self.template, self.context)
    text_content = strip_tags(html_content)
    message = EmailMultiAlternatives(
        self.subject,
        text_content,
        from_email,
        recipients
    )
    message.attach_alternative(html_content, 'text/html')
    message.send(fail_silently=False)
    
