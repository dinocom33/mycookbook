from django.contrib.auth import get_user_model
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
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'Comments'
