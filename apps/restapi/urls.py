from django.urls import path
from .views import (
    UserCreateView, 
    UserUpdateDeleteView,
    ContactListView,
    ContactCreateView,
    ContactUpdateDeleteView,
    DebtCreateView,
    DebtListView,
    DebtDetailUpdateDestroyView,
    CurrencyCreateView,
    DebtPaidView,
    CurrencyListView,
)

urlpatterns = [
    #users
    path("users/", UserCreateView.as_view(), name='user_create'),
    path("users/profile/", UserUpdateDeleteView.as_view(), name='user_update_delete'),

    #contacts
    path("contacts/", ContactCreateView.as_view(), name='contact_create'),
    path("contacts/list/", ContactListView.as_view(), name='contact_list'),
    path("contacts/<int:pk>/", ContactUpdateDeleteView.as_view(), name='contact_update_delete'),

    #debt
    path("debts/", DebtCreateView.as_view(), name='debt_create'),
    path("debts/list/", DebtListView.as_view(), name='debt_list'),
    path("debts/<int:pk>/", DebtDetailUpdateDestroyView.as_view(), name='debt_detail'),
    path("debts/<int:pk>/paid/", DebtPaidView.as_view(), name='paying_debt'),

    #currency
    path("currencies/", CurrencyCreateView.as_view(), name='currency_create'),
    path("currencies/list/", CurrencyListView.as_view(), name='currency_list'),
]
