# Generated by Django 4.2.1 on 2023-07-15 08:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(error_messages={'invalid': 'Please, enter a valid email address!'}, max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='Email'),
        ),
    ]
