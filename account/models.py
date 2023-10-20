from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from account.managers import CustomAccountManager
from django.contrib.auth.models import PermissionsMixin


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)   # Я хотел реализовать тут is_active = False, и после верификации этот парамент должен изменить на True,
                                                    # но тк по умолчанию тут должно быть False, я не могу получить user = authenticate (во views, метод post)
                                                    # он отдает мне user = None
                                                    # поэтому этот параметр оставил в True, чтобы проверить код


                                                    # по видеоуроку автор для активации использует парамеметр email_verify = False
                                                    #  (смотри account/forms.py - class AuthenticationForm(DjangoAuthenticationForm)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True, default=None)

    account = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
