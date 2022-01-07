from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PROJECT.settings")

app = Celery("PROJECT")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-to-users': {
        'task': 'send_financial_report',
        'schedule': crontab(0, 0, day_of_month='28'),
    },
    'send-report-now': {
        'task': 'send_financial_report',
        'schedule': crontab(hour=19, minute=20),
    },
}
