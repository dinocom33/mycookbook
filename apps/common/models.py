from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from apps.recipes.models import Recipe

UserModel = get_user_model()


class CommentsModel(models.Model):
    text = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Comment',
    )

    published_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'Comments'


class Contact(models.Model):
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    email = models.EmailField(
        max_length=100,
        null=False,
        blank=False,
        validators=[
            validators.EmailValidator(),
        ],
        verbose_name='Email',

    )

    subject = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Subject',
    )

    message = models.TextField(
        null=False,
        blank=False,
        verbose_name='Message',
    )

    date_sent = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Contact forms'
        verbose_name_plural = 'Contact forms'

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.email
