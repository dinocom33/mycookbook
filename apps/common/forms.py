from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from apps.common.models import CommentsModel


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'placeholder': 'Username',
                                      'class': 'form-control',
                                      }))
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(attrs={'placeholder': 'Email',
                                      'class': 'form-control',
                                      }))
    password1 = forms.CharField(max_length=20,
                                required=True,
                                label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=20,
                                required=True,
                                label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("The email already exists")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

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
