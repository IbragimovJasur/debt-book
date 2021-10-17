from django.urls import path
from .views import (
    UserCreateView, 
    UserUpdateDeleteView,
    ContactListView,
    ContactCreateView,
    ContactUpdateDeleteView,
)

urlpatterns = [
    #users
    path("user/create/", UserCreateView.as_view(), name='user_create'),
    path("user/<int:pk>/update-delete/", UserUpdateDeleteView.as_view(), name='user_update_delete'),

    #contacts
    path("contacts/", ContactListView.as_view(), name='contact_list'),
    path("contacts/create/", ContactCreateView.as_view(), name='contact_create'),
    path("contacts/<int:pk>/update-delete/", ContactUpdateDeleteView.as_view(), name='contact_update_delete'),
]
