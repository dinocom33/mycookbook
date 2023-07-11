# Generated by Django 4.2.1 on 2023-07-07 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_favoriterecipemodel_rating_recipe_favorites'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0005_alter_commentsmodel_recipe_alter_commentsmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='recipe_likes', to='recipes.recipe')),
                ('user', models.ManyToManyField(related_name='user_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
