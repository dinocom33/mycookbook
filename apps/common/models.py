from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator, MinLengthValidator
from django.db import models

from apps.common.validators import contact_names_validator
from apps.recipes.models import Recipe

UserModel = get_user_model()


class CommentsModel(models.Model):
    TEXT_MAX_LENGTH = 300

    text = models.CharField(
        max_length=TEXT_MAX_LENGTH,
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
        return f'{self.user} - {self.recipe.title}'

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'Comments'


class Contact(models.Model):
    FIRST_NAME_MAX_LENGTH = 100
    LAST_NAME_MAX_LENGTH = 100
    EMAIL_MAX_LENGTH = 50
    SUBJECT_MAX_LENGTH = 100

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        verbose_name='First Name',
        validators=[
            contact_names_validator,
        ],
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        verbose_name='Last Name',
        validators=[
            contact_names_validator,
        ],
    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LENGTH,
        null=False,
        blank=False,
        verbose_name='Email',
        validators=[
            EmailValidator(message='Please, enter a valid email address!'),
        ],
    )

    subject = models.CharField(
        max_length=SUBJECT_MAX_LENGTH,
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(5, 'Subject must be at least 5 characters long!'),
        ],
        verbose_name='Subject',
    )

    message = models.TextField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(10, 'Message must be at least 10 characters long!'),
        ],
        error_messages={
            'required': 'Please, enter a message!',
        },
        verbose_name='Message',
    )

    date_sent = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'Contact form'
        verbose_name_plural = 'Contact forms'

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.email
