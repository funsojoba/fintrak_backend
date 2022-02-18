from typing import Dict

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailManager:
    from_email = settings.EMAIL_FROM

    def __init__(self, template=None, subject=None, recipients=[], context={}):
        self.template = template
        self.recipients = recipients
        self.context = context
        self.subject = subject

    def _compose_mail(self):
        html_content = render_to_string(self.template, self.context)
        text_content = strip_tags(html_content)
        message = EmailMultiAlternatives(
            self.subject,
            text_content,
            self.from_email,
            self.recipients,
        )
        message.attach_alternative(html_content, 'text/html')
        return message

    def send(self):
        mail = self._compose_mail()
        result = mail.send(fail_silently=False)
        return result
