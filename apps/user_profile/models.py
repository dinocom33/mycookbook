from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image

from django.contrib.auth.models import User

from apps.user_profile.validators import first_and_last_name_validator

UserModel = get_user_model()


class Profile(models.Model):

    FIRST_NAME_MAX_LENGTH = 100
    LAST_NAME_MAX_LENGTH = 100

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=[
            first_and_last_name_validator,
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=[
            first_and_last_name_validator,
        ]
    )

    avatar = models.ImageField(
        upload_to='profile_images',
        default='profile_images/default.jpg',
        null=True,
        blank=True,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:

            img = Image.open(self.avatar.path)

            if img.height > 200 or img.width > 200:
                new_img = (200, 200)
                img.thumbnail(new_img)
                img.save(self.avatar.path)

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.user.username
