from django.contrib import messages
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


def logged_in_message(sender, user, request, **kwargs):
    if user.profile.first_name and user.profile.last_name:
        messages.info(request, f"Welcome {user.profile.first_name} {user.profile.last_name}!")
    else:
        messages.info(request, f"Welcome {user.username}!")


user_logged_in.connect(logged_in_message)
