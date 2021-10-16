from django.contrib import admin
from .models import Currency

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol']
    list_display_links = ['name']
