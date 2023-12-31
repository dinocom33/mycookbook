from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from apps.common.models import CommentsModel, Contact


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        required=True,
        label='Username',
        widget=forms.TextInput(
            attrs={'placeholder': 'Username',
                   'class': 'form-control',
                   }))
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(
            attrs={'placeholder': 'Email',
                   'class': 'form-control',
                   }))

    password1 = forms.CharField(
        max_length=20,
        required=True,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                   'class': 'form-control',
                   'data-toggle': 'password',
                   'id': 'password',
                   }))
    password2 = forms.CharField(
        max_length=20,
        required=True,
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm Password',
                   'class': 'form-control',
                   'data-toggle': 'password',
                   'id': 'password',
                   }))

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError(f"The email {email} is already registered.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise ValidationError(f"The username {username} is already taken.")
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Username',
                   'class': 'form-control',
                   }))
    password = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                   'class': 'form-control',
                   'data-toggle': 'password',
                   'id': 'password',
                   'name': 'password',
                   }))
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput()
    )

    def clean_username(self):
        username = self.cleaned_data['username']

        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise forms.ValidationError(f"User '{username}' does not exist. Please try again.")

    def confirm_login_allowed(self, user):
        password = self.cleaned_data['password']
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password. Please try again.")

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentsModel
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 161,
                    'rows': 2,
                    'placeholder': 'Add your comment...'
                },
            ),
        }
        labels = {
            'text': 'Add Comment',
        }


class SearchForm(forms.Form):
    recipe = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search...'
            }
        )
    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['date_sent', ]
        widgets = {
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Add your message...'
                }),
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Subject...'
                }),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email...'
                }),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name...'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name...'
                }),
        }
        error_messages = {
            'email': {
                'invalid': 'Please, enter a valid email address!',
            },
            'subject': {
                'required': 'Subject field is required!',
            },
            'message': {
                'required': 'Message field is required!',
            },
        }
