# Generated by Django 4.2.1 on 2023-07-17 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0024_images_delete_recipeimages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Images',
        ),
    ]
