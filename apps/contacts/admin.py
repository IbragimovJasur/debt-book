from django.contrib import admin
from .models import Currency, Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['username', 'debt_currency','debt_amount', 'debt_end_on', ]
    list_display_links = ['username']

admin.site.register(Currency)
