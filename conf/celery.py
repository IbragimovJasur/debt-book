import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery('conf')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # Execute daily at midnight.
    'remind_debt_deadline': {
        'task': 'apps.users.remind_debt_deadline',
        'schedule': crontab(minute=0, hour=0),
    },
    #Execute every minute.
    'debt_paid_notification': {
        'task': 'apps.users.debt_paid_notification',
        'schedule': crontab(),
    },
}
