from django.urls import path

from .views import edit_profile, ChangePasswordView

urlpatterns = [
    path('edit/<int:pk>/', edit_profile, name='edit profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password change'),
]
