from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUser(AbstractUser):
    class Meta:
        db_table='customusers'

    email = models.EmailField(
        "Email address", unique=True)
    avatar = models.ImageField(
        "Profile photo", upload_to='users/avatar/', default='users/avatar/default.jpg')
    phone_number = models.CharField(
        "Phone number", max_length=150, unique=True)
    sms_code = models.CharField(
        "SMS code that user receives", max_length=5, null=True, blank=True)
    created_at = models.DateTimeField(
        "When user is joined", auto_now_add=True)
    updated_at = models.DateTimeField(
        "When user profile is updated", auto_now=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username

