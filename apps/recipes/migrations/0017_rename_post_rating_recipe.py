# Generated by Django 4.2.1 on 2023-07-13 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0016_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='post',
            new_name='recipe',
        ),
    ]
