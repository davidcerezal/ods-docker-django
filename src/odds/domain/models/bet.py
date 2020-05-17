from django.db import models
from .betMarket import BetMarket
from .betType import BetType


class Bet(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    price = models.FloatField(blank=True)
    value = models.CharField(max_length=20, blank=True)
    expiry_date = models.DateTimeField()
    contra_bet = models.ManyToManyField('self', blank=True)
    market = models.ManyToManyField(BetMarket, blank=True)
    type = models.ManyToManyField(BetType)
    revised = models.BooleanField()

    def __str__(self):
        return self.name