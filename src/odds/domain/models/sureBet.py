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

    def isExpired(self):
        for event in self.events.all():
            if event.isExpired():
                return True
        return False

    def getGloblaType(self):
        different_types = dict()
        for bet in self.bets.all():
            if bet.type.all()[0].identifier not in different_types.keys():
                different_types[bet.type.all()[0].identifier] = bet.type.all()[0].identifier

        if len(different_types) == 3:
            return 'third_type'
        if len(different_types) == 2:
            return 'second_type'
        else:
            return 'none_type'

    def getBestBetByType(self, type, npos=0):
        if len(self.bets.filter(type=type).order_by('-price')) > npos:
            return self.bets.filter(type=type).order_by('-price')[npos]
        else:
            return ''

