# Generated by Django 4.2.4 on 2023-10-24 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_email_verify'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_active',
        ),
    ]
