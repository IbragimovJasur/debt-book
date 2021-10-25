from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from apps.main.models import Currency
from apps.contacts.models import Contact
from django.conf import settings

class User(AbstractUser):
    class Meta:
        db_table='users'

    phone = models.CharField(
        "Phone number", max_length=150, unique=True
    )
    avatar = models.ImageField(
        "Profile photo", upload_to='users/avatar/', default='users/avatar/default.jpg'
    )
    sms_code = models.CharField(
        "SMS code", max_length=5, null=True, blank=True
    )

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']


class Debt(models.Model):
    LENT = 1  # Lent
    BORROW = 2  # Borrowed

    TYPE_DEBT = (
        (LENT, "Lend"),
        (BORROW, "Borrow"),
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='debts', on_delete=models.CASCADE, null=True
    )
    contact = models.ForeignKey(
        Contact, verbose_name='Contact', related_name='debts', on_delete=models.CASCADE, null=True
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, related_name='debts', null=True
    )
    amount = models.IntegerField(
        "Amount"
    )
    type_debt = models.IntegerField(
        "Type", choices=TYPE_DEBT, default=2
    )
    started_on = models.DateTimeField(
        "Date when it was given/taken", null=True, blank=True
    )
    end_on = models.DateTimeField(
        "Date when it has to be returned", null=True, blank=True
    )
    comment = models.TextField(
        "Comment", null=True, blank=True
    )
    paid = models.BooleanField(
        "Is returned", default=False
    )
    paid_at = models.DateTimeField(
        "Is returned at", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid_at_auto = models.DateTimeField(
        null=True, blank=True
    )

    class Meta:
        db_table = "debts"

    def __str__(self):
        return self.contact.owner.username
    
    def is_lent(self):
        return self.type_debt == 1

    def get_amount(self):
        return self.amount