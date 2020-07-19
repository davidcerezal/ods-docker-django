from django.db import models
from .bet import Bet
from .event import Event
import uuid

class SureBet(models.Model):

    TYPE_NORMAL = 'normal'
    TYPE_COMBINED = 'combined'

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True)
    uuid = models.CharField(max_length=255,  blank=True, unique=True, default=uuid.uuid4)
    value = models.CharField(max_length=20, blank=True)
    benefit = models.FloatField(max_length=20, blank=True)
    bets = models.ManyToManyField(Bet, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    revised = models.BooleanField(default=False)
    combined_bets_first = models.ManyToManyField(Bet, blank=True, related_name='firs_combined')
    combined_bets_second = models.ManyToManyField(Bet, blank=True, related_name='second_combined')

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

