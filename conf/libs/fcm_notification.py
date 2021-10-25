from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice


def send_notification(to_whom, title, message, image=''):
    devices = FCMDevice.objects.filter(user=to_whom)
    if devices:
        devices.send_message(
            Message(notification=Notification(title=title, body=message, image=image))
        )
