from celery import shared_task
from datetime import datetime
from authentication.models.user import User
from .views import generate_report


@shared_task(name="send_financial_report")
def finance_report():
        users = User.objects.all()
        for user in users:
                generate_report(user)
        




