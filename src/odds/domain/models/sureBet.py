from django.db import models
from .bet import Bet


class SureBet(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    value = models.CharField(max_length=20)
    benefit = models.CharField(max_length=20)
    bets = models.ManyToManyField(Bet)
    revised = models.BooleanField()

    def __str__(self):
        return self.name
