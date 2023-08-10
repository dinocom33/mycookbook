from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import LoginForm
from .views import RegisterView, UserLoginView, IndexView, AboutView, contact_view, EmailSentView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('email-sent', EmailSentView.as_view(), name='email sent'),
    path('login/', UserLoginView.as_view(redirect_authenticated_user=True, template_name='common/login.html',
                                         authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', contact_view, name='contact'),
]
