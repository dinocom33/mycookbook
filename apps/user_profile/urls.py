from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path

from .views import edit_profile, ChangePasswordView, ResetPasswordView, ResetPasswordConfirm

urlpatterns = [
    path('edit/<int:pk>/', edit_profile, name='edit profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password change done'),
    path('password-reset/', ResetPasswordView.as_view(), name='password reset'),
    path('password-reset-confirm/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='password_reset_confirm'),
]
