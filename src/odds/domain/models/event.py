from datetime import datetime
from django.utils import timezone
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
    revised = models.BooleanField()

    def __str__(self):
        return self.name

    def getBestBetByType(self, type, npos=0):
        if len(self.bets.filter(type=type).order_by('-price')) > npos:
            return self.bets.filter(type=type).order_by('-price')[npos]
        else:
            return ''

    def isExpired(self):
        return True if self.date < timezone.now() else False

