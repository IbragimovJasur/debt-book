from django.contrib import admin
from .models import Currency, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['owner', 'username']
    list_display_links = ['owner']
