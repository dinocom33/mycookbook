# Generated by Django 4.2.1 on 2023-07-31 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0028_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator('Please, enter a valid email address!!!')], verbose_name='Email'),
        ),
    ]
