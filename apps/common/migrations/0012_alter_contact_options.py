# Generated by Django 4.2.1 on 2023-07-14 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_alter_contact_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact form', 'verbose_name_plural': 'Contact forms'},
        ),
    ]