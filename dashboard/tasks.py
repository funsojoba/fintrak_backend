from celery import shared_task
from datetime import datetime
from authentication.models.user import User


@shared_task(name="finance_report")
def finance_report():
        users = User.objects.all()
        
        for user in users:
                pass
        
        current_month = datetime.now().month




