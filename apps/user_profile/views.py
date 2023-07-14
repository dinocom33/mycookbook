from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UpdateUserForm, UpdateProfileForm


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

    return render(request, 'user_profile/profile.html', context)


class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = 'user_profile/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('edit profile')
