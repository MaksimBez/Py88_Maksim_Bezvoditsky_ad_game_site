# Generated by Django 4.2.4 on 2023-09-02 10:17

import account.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', account.managers.CustomAccountManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('phone', models.CharField(default=None, max_length=255, unique=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
