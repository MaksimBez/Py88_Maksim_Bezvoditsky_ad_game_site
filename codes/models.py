from django.db import models
from account.models import Account
from prizes.models import Prizes


class UsersCodes(models.Model):
    code = models.CharField(max_length=12, unique=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class UsersTransactions(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prizes, on_delete=models.CASCADE)

