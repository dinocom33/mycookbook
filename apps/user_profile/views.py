from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DeleteView

from .forms import UpdateUserForm, UpdateProfileForm, ChangePasswordForm, ResetPasswordForm

UserModel = get_user_model()


@login_required
def edit_profile(request, pk):
    user = User.objects.filter(pk=pk).get()
    profile = user.profile

    if request.method == 'GET':
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)
    else:
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=user.profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect(to='edit profile', pk=pk)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user': user,
    }

    return render(request, 'user_profile/edit-profile.html', context)


class ChangePasswordView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_message = "Successfully Changed Your Password. Please login with your new password."
    success_url = reverse_lazy('logout')

    def test_func(self):
        return self.request.user == UserModel.objects.get(pk=self.kwargs['pk'])

    def handle_no_permission(self):
        raise Http404


class ResetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'registration/reset-password.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class DeleteUserView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = UserModel
    template_name = 'user_profile/user-confirm-delete.html'
    success_message = f"Successfully deleted your account."
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user == UserModel.objects.get(pk=self.kwargs['pk'])

    def handle_no_permission(self):
        raise Http404
