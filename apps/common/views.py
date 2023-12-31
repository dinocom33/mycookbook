from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django_email_verification import send_email

from .forms import RegisterForm, LoginForm, ContactForm

from ..recipes.models import Recipe

UserModel = get_user_model()


class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all().order_by('-created_at')[:3]

        context = {
            'recipes': recipes,
        }

        return render(request, 'common/index.html', context)


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'common/register.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save(commit=False)
        user_email = form.cleaned_data['email']
        user_username = form.cleaned_data['username']
        user_password = form.cleaned_data['password1']

        user = UserModel.objects.create_user(username=user_username, email=user_email, password=user_password)

        user.is_active = False
        send_email(user)

        return HttpResponseRedirect(reverse('email sent'))

    def form_invalid(self, form):
        return super().form_invalid(form)


class EmailSentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/email-sent.html')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'common/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='index')

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(UserLoginView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('edit profile', args=[self.request.user.pk])


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'common/about.html')


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'common/success.html')

    context = {
        'form': form,
    }

    return render(request, 'common/contact.html', context)
