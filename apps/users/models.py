from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from apps.main.models import Currency
from apps.contacts.models import Contact

class User(AbstractUser):
    class Meta:
        db_table='users'

    phone_number = models.CharField(
        "Phone number", max_length=150, unique=True)
    avatar = models.ImageField(
        "Profile photo", upload_to='users/avatar/', default='users/avatar/default.jpg')
    sms_code = models.CharField(
        "SMS code that user receives", max_length=5, null=True, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']


class Debt(models.Model):
    class Meta:
        db_table = "debts"

    TYPE_CHOICES = [
        ("lent", "Lend"),
        ("borrowed", "Borrow"),
        ("paid", "Paid"),
    ]
    contact = models.ForeignKey(
        Contact, verbose_name='Contact', related_name='debts', on_delete=models.CASCADE, null=True)
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, related_name='debts', null=True)
    amount = models.IntegerField(
        "Amount")
    type = models.CharField(
        "Type", choices=TYPE_CHOICES, max_length=50)
    started_on = models.DateTimeField(
        "Date when it was given/taken")
    end_on = models.DateTimeField(
        "Date when it has to be returned")
    comment = models.TextField(
        "Comment", null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.contact.owner.username
    
    def get_amount(self):
        return self.amount
    