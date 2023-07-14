# from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from django.db.models import Avg
from django.shortcuts import reverse

UserModel = get_user_model()


class Recipe(models.Model):

    CATEGORY_CHOICES = (
        ('salads', 'Salads'),
        ('soups', 'Soups'),
        ('main_dishes', 'Main Dishes'),
        ('bbq', 'BBQ'),
        ('deserts', 'Desserts'),
    )

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Recipe Title',
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        verbose_name='Ingredients',
    )

    instructions = models.TextField(
        null=False,
        blank=False,
        verbose_name='Cooking Instructions',
    )

    created_by = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    category = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        choices=CATEGORY_CHOICES,
        verbose_name='Recipe Category',
    )

    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL',
    )

    slug = AutoSlugField(
        populate_from='title',
    )

    favorites = models.ManyToManyField(
        UserModel,
        through='FavoriteRecipeModel',
        related_name='favorite_recipes'
    )

    def get_absolute_url(self):
        return reverse('recipe details', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })

    def average_rating(self) -> float:
        return Rating.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return self.title


class FavoriteRecipeModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Favorite Recipes'
        verbose_name_plural = 'Favorite Recipes'

    def __str__(self):
        return f"{self.user} - {self.recipe.title}"


class LikedRecipe(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    liked_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Likes'
        verbose_name_plural = 'Recipe Likes'

    def __str__(self):
        return self.recipe.title + " liked by " + self.user.username


class Rating(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )

    rating = models.IntegerField(
        default=0,
    )

    class Meta:
        verbose_name = 'Recipe Rating'
        verbose_name_plural = 'Recipe Ratings'
        unique_together = ['user', 'recipe']

    def __str__(self):
        return f"{self.recipe.title}: {self.rating}"
