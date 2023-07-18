# Generated by Django 4.2.1 on 2023-07-18 09:53

import apps.recipes.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0028_favoriterecipemodel_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_images', validators=[apps.recipes.validators.file_size_validator]),
        ),
    ]
