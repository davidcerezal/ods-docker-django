from django.db import models
from .bet import Bet


class SureBet(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    value = models.CharField(max_length=20, blank=True)
    benefit = models.CharField(max_length=20, blank=True)
    bets = models.ManyToManyField(Bet, blank=True)
    revised = models.BooleanField()

    def __str__(self):
        return self.name
