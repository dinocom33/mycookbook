# Generated by Django 4.2.1 on 2023-07-07 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_like_recipe_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoriterecipemodel',
            name='rating',
        ),
    ]
