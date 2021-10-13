from django.urls import path
from .views import CustomUserCreateView, CustomUserUpdateDeleteView

urlpatterns = [
    #users
    path("user/create/", CustomUserCreateView.as_view(), name='user_create'),
    path("user/<int:pk>/update-delete/", CustomUserUpdateDeleteView.as_view(), name='user_update_delete'),
]
