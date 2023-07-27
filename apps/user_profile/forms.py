from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               disabled=True,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control'
                             }))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                                 required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    avatar = forms.ImageField(required=False,
                              widget=forms.FileInput(attrs={
                                  'class': 'form-control-file'
                              }))
    bio = forms.CharField(required=False,
                          widget=forms.Textarea(attrs={
                              'class': 'form-control', 'rows': 5
                          }))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar', 'bio']


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['old_password', 'new_password1', 'new_password2']


class ResetPasswordForm(PasswordResetForm):

    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']
