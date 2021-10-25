import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Execute daily at midnight.
    'send-debt-return-notification': {
        'task': 'apps.users.remind_debt_deadline',
        'schedule': crontab(minute=0, hour=0),
    },
}
