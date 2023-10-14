from django.db import models


class Prizes(models.Model):
    prize = models.CharField(max_length=255, unique=True)
    cost = models.CharField(max_length=2)



