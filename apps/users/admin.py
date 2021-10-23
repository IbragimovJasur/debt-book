from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Debt

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ['contact', 'amount', 'end_on']
    list_display_links = ['contact']

class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'phone', ]

admin.site.register(User, UserAdmin)