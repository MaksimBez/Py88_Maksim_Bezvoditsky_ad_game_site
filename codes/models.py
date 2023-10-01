from django.db import models
from account.models import Account


class UsersCodes(models.Model):
    code = models.CharField(max_length=12, unique=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)

