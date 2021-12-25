from typing import Dict

import requests
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class EmailManager:
    from_email = settings.EMAIL_FROM

    def __init__(self, template=None, subject=None, recipients=[], context={}):
        self.template = template
        self.recipients = recipients
        self.context = context
        self.subject = subject

    def _compose_mail(self):
        message = EmailMessage(
            subject=self.subject,
            body=render_to_string(self.template, self.context),
            from_email=self.from_email,
            to=self.recipients,
            bcc=settings.SUPER_ADMIN_MAIL_LIST,
        )
        message.content_subtype = "html"
        return message

    def send(self):
        mail = self._compose_mail()
        result = mail.send(fail_silently=False)
        return result
