from django.db import models
from django.conf import settings

class Contact(models.Model):
    class Meta:
        db_table = "contacts"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts', null=True, blank=True)
    name = models.CharField(
        "Username", max_length=150)
    avatar = models.ImageField(
        "Profile photo", upload_to='users/avatar/', default='users/avatar/default.jpg')
    phone = models.CharField(
        "Phone number", max_length=50)
    card_number = models.CharField(
        "Card number", max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(
        "When contact is created", auto_now_add=True)
    updated_on = models.DateTimeField(
        "When contact is updated", auto_now=True)
   
    def __str__(self):
        return self.owner.username
