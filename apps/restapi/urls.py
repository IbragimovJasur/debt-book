from django.urls import path
from .views import (
    CustomUserCreateView, 
    CustomUserUpdateDeleteView,
    ContactListView,
    ContactCreateView,
    ContactUpdateDeleteView,
)

urlpatterns = [
    #users
    path("user/create/", CustomUserCreateView.as_view(), name='user_create'),
    path("user/<int:pk>/update-delete/", CustomUserUpdateDeleteView.as_view(), name='user_update_delete'),

    #contacts
    path("contacts/", ContactListView.as_view(), name='contact_list'),
    path("contacts/create/", ContactCreateView.as_view(), name='contact_create'),
    path("contacts/<int:pk>/update-delete/", ContactUpdateDeleteView.as_view(), name='contact_update_delete'),
]
