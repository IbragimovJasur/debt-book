from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Debt

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ['owner', 'contact', 'amount', 'end_on']
    list_display_links = ['owner']

class UserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'phone', ]

admin.site.register(User, UserAdmin)