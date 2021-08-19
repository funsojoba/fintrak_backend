from decouple import config
from django.core.mail import send_mail


class MailUtil:
    @staticmethod
    def send_mail(data):
        email_subject = data['email_subject']
        message = data['email_body']
        email_from = config('EMAIL_HOST_USER', default='noreply.dummy@gmail.com')
        email_to = data['email_to']
        html_format = data['email_body']

        try:
            send_mail(email_subject, message, email_from, email_to, fail_silently=False, html_message=html_format)
            return True
        except Exception as err:
            print(str(err))
            return False
