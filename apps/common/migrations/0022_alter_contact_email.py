# Generated by Django 4.2.1 on 2023-07-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(error_messages={'invalid': 'Please, enter a valid email address!'}, max_length=50, verbose_name='Email'),
        ),
    ]