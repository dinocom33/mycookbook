from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Contact


def send_contact_email(contact_form):
    send_mail(
        subject=contact_form.subject,
        message=contact_form.message,
        from_email=contact_form.email,
        recipient_list=['simeon.s.todorov@gmail.com'],
    )


@receiver(post_save, sender=Contact)
def contact_email_created(sender, instance, created, **kwargs):
    send_contact_email(instance)
