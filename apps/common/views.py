from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from .forms import RegisterForm, LoginForm
from ..recipes.models import Recipe, FavoriteRecipeModel


class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all().order_by('-updated_at')[:3]

        context = {
            'recipes': recipes,
        }

        return render(request, 'common/index.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'common/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='index')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'common/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='index')

        return super(UserLoginView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('edit profile', args=[self.request.user.pk])


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'common/about.html')
