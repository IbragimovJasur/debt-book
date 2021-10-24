from datetime import datetime, timezone

def check_send_notification(data):
    # проверка на остаток дня для уведомлений
    end_on = data['end_on']
    today = datetime.today(timezone.utc)
    return end_on - today
