from rest_framework.permissions import BasePermission
from apps.contacts.models import Contact
from apps.users.models import Debt

class IsContactOwner(BasePermission):
    def has_permission(self, request, view):
        try:
            contact= Contact.objects.get(pk=view.kwargs.get('pk'))
            return request.user == contact.owner
        except:
            return False

class IsDebtOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        debt= Debt.objects.get(pk= view.kwargs.get('pk')) 
        return request.user == debt.contact.owner
