# Generated by Django 4.2.1 on 2023-07-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0020_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(error_messages={'required': 'Please, enter a subject!'}, max_length=100, verbose_name='Subject'),
        ),
    ]
