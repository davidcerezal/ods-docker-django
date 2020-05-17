from django.db import models
from .bet import Bet

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    player1 = models.CharField(max_length=255, blank=True)
    player2 = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField()
    bets = models.ManyToManyField(Bet, blank=True)
    betable = models.BooleanField()

    def __str__(self):
        return self.name

