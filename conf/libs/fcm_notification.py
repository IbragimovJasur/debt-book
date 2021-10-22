from datetime import datetime, timezone, timedelta
from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice
from apps.users.models import Debt

def send_notification(debt_model):
    today = datetime.now(timezone.utc)
    if debt_model.end_on.date() - today.date() == timedelta(days=5):
        devices = FCMDevice.objects.get(user=debt_model.contact.owner)
        if debt_model.type == 'lent':
            devices.send_message(
                Message(
                    notification=Notification(title="5 days left", body="text", image="url"),
                    topic= f"{debt_model.contact.name} need to return debt to you till {debt_model.end_on}",
                ))
        elif debt_model.type == 'borrowed':
            devices.send_message(
                Message(
                    notification=Notification(title="5 days left", body="text", image="url"),
                    topic= f"You need to return debt to {debt_model.contact.name} till {debt_model.end_on}",
                ))
