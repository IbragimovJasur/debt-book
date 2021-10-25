import apps.users.models as user_models
from conf.celery import app
from apps.main.logics import check_date
from conf.libs.fcm_notification import send_notification


@app.task
def remind_debt_deadline():
    debts = user_models.Debt.objects.all()
    for debt in debts:
        if check_date(debt.end_on) and not debt.paid:
            if debt.is_lent(): 
                send_notification(
                    debt.owner, 
                    "Return the debt", 
                    f"Today {debt.contact.name} has to return {debt.currency}{debt.get_amount()}"
                )
            
            else:
                send_notification(
                    debt.owner, 
                    "Return the debt", 
                    f"Today you have to return {debt.currency}{debt.get_amount()} to {debt.contact.name}"
                )


@app.task
def debt_paid_notification():
    debts = user_models.Debt.objects.all()
    for debt in debts:
        if debt.paid and debt.contact.is_user():
            send_notification(
                debt.contact.get_contact_user(),
                "Debt is returned",
                f"{debt.contact.owner} is returned {debt.currency}{debt.get_amount()} debt"
            )
