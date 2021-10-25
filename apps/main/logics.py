from datetime import datetime, timezone, timedelta


def check_date(end_on):
    today = datetime.now(timezone.utc)
    return end_on - today.date() < timedelta(days=1)
