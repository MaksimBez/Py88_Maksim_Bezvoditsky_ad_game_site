from django.db import models


class Prize(models.Model):
    prize = models.CharField(max_length=255, unique=True)
    cost = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.prize}'
