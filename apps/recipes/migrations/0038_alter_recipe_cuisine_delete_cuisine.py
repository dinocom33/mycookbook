# Generated by Django 4.2.1 on 2023-08-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0037_alter_cuisine_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(blank=True, choices=[('mexican', 'Mexican Recipes'), ('italian', 'Italian Recipes'), ('american', 'American Recipes'), ('indian', 'Indian Recipes'), ('french', 'French Recipes'), ('japanese', 'Japanese Recipes'), ('chinese', 'Chinese Recipes'), ('korean', 'Korean Recipes'), ('thai', 'Thai Recipes'), ('spanish', 'Spanish Recipes')], max_length=8, null=True),
        ),
        migrations.DeleteModel(
            name='Cuisine',
        ),
    ]
