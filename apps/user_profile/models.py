from django.contrib.auth import get_user_model
from django.db import models
from PIL import Image

from django.contrib.auth.models import User

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    avatar = models.ImageField(
        default='default.jpg',
        upload_to='profile_images',
        null=True,
        blank=True
    )

    bio = models.TextField(
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
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
