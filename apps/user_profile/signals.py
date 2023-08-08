from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from mycookbook import settings
from .models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(pre_save, sender=UserModel, dispatch_uid='active')
def send_greeting_email(sender, instance, **kwargs):
    if instance.is_active and UserModel.objects.filter(pk=instance.pk, is_active=False).exists():
        subject = 'Welcome to My Cook Book'
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]

        context = {'username': instance.username}
        html_message = render_to_string('emails/welcome-email.html', context)
        text_message = strip_tags(html_message)

        email = EmailMultiAlternatives(subject, text_message, from_email, to_email)
        email.attach_alternative(html_message, "text/html")
        email.send()


def logged_in_message(sender, user, request, **kwargs):
    if user.profile.first_name and user.profile.last_name:
        messages.info(request, f"Welcome {user.profile.first_name} {user.profile.last_name}!")
    else:
        messages.info(request, f"Welcome {user.username}!")


user_logged_in.connect(logged_in_message)
