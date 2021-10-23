from datetime import datetime, timezone, timedelta
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice

def check_date(end_on, days):
    today = datetime.now(timezone.utc)
    return end_on - today.date() == timedelta(days=1)


def send_notification(owner, title, message, image=''):
    devices = FCMDevice.objects.filter(user=owner)
    devices.send_message(
        Message(notification=Notification(title=title, body=message, image=image))
    )
