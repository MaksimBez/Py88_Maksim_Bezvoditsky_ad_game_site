# Generated by Django 4.2.4 on 2023-10-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email_verify',
            field=models.BooleanField(default=False),
        ),
    ]