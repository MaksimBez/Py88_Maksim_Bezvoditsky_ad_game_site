from django.db import models
from account.models import Account
from prize.models import Prize


class UserPromocode(models.Model):
    promocode = models.CharField(max_length=12, unique=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class UserTransaction(models.Model):

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
