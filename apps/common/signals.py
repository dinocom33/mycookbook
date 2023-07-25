from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from mycookbook import settings
from .models import Contact


@receiver(post_save, sender=Contact)
def send_contact_submission_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Contact Form Submission'
        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.CONTACT_FORM_EMAIL]

        context = {
            'name': instance.first_name + ' ' + instance.last_name if instance.first_name and instance.last_name else instance.email,
            'email': instance.email,
            'subject': instance.subject,
            'message': instance.message,
        }
        html_message = render_to_string('emails/contact-form-template.html', context)
        text_message = strip_tags(html_message)

        email = EmailMultiAlternatives(subject, text_message, from_email, to_email)
        email.attach_alternative(html_message, "text/html")
        email.send()
