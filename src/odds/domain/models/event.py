from django.db import models
from .bet import Bet

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    player1 = models.CharField(max_length=255)
    player2 = models.CharField(max_length=255)
    date = models.DateTimeField()
    bets = models.ForeignKey(Bet, on_delete=models.CASCADE)
    betable = models.BooleanField()

    def __str__(self):
        return self.name

