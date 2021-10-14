from django.db import models
from django.conf import settings

class Currency(models.Model):
    name = models.CharField(
        "Sign of currency", max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    class Meta:
        db_table = "contacts"

    DEBT_TYPE_CHOICES = [
        ("lent", "Lend"),
        ("borrowed", "Borrow"),
        ("paid", "Paid"),
    ]
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    debt_currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, blank= True)
    username = models.CharField(
        "Username", max_length=150)
    phone = models.CharField(
        "Phone number", max_length=50)
    address = models.CharField(
        "Address", max_length=250, null=True, blank=True)
    comment = models.TextField(
        "Any comment about contact", null=True, blank=True)
    card_number = models.CharField(
        "Card number", max_length=100, null=True, blank=True)
    debt_type = models.CharField(
        "Type of debt", choices=DEBT_TYPE_CHOICES, max_length=50)
    debt_started_on = models.DateTimeField(
        "Date when debt was given/taken")
    debt_end_on = models.DateTimeField(
        "Date when debt should be returned")
    debt_amount = models.IntegerField(
        "Debt amount")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username
