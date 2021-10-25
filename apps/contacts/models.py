from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Contact(models.Model):
    class Meta:
        db_table = "contacts"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contacts', null=True, blank=True)
    name = models.CharField(
        "Name", max_length=150, null=True)
    avatar = models.ImageField(
        "Profile photo", upload_to='contacts/avatar/', default='contacts/avatar/default.jpg')
    phone = models.CharField(
        "Phone number", max_length=50)
    card_number = models.CharField(
        "Card number", max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(
        "When contact is created", auto_now_add=True)
    updated_on = models.DateTimeField(
        "When contact is updated", auto_now=True)
   
    def __str__(self):
        return f"{self.owner.username}-{self.name}"

    def is_user(self):
        try:
            user = get_user_model().objects.get(phone=self.phone)
            return True
        except: return False

    def get_contact_user(self):
        contact_user = get_user_model().objects.get(phone=self.phone)
        return contact_user
