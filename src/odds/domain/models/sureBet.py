from django.db import models
from .bet import Bet
from .event import Event
import uuid


class SureBet(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255,  blank=True, unique=True, default=uuid.uuid4)
    value = models.CharField(max_length=20, blank=True)
    benefit = models.FloatField(max_length=20, blank=True)
    bets = models.ManyToManyField(Bet, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    revised = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def getTypes(self):
        betsTypes = []
        for bet in self.bets.all():
            betsTypes.append(bet.type.all()[0])
        return betsTypes

    def getBestBetByType(self, type):
        best_bet_ratio = best_bet = 0
        for bet in self.bets.filter(type=type):
            if bet.price > best_bet_ratio:
                best_bet = bet
        return best_bet

