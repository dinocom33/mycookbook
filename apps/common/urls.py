from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import LoginForm
from .views import RegisterView, UserLoginView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(redirect_authenticated_user=True, template_name='common/login.html',
                                         authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
