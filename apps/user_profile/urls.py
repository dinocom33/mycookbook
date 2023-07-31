from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import path

from .views import edit_profile, ChangePasswordView, ResetPasswordView, DeleteUserView

urlpatterns = [
    path('edit/<int:pk>/', edit_profile, name='edit profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password change'),
    path('password-reset/', ResetPasswordView.as_view(), name='password reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/reset-password-confirm.html'
    ), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(
        template_name='registration/password-reset-complete.html'
    ), name='password_reset_complete'),
    path('delete-account/<int:pk>/', DeleteUserView.as_view(), name='delete account'),
]
