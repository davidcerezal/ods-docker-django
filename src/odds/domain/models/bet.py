from django.db import models
from .betMarket import BetMarket
from .betType import BetType


class Bet(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    price = models.FloatField()
    value = models.CharField(max_length=20)
    expiry_date = models.DateTimeField()
    contra_bet = models.ManyToManyField('self')
    market = models.ManyToManyField(BetMarket)
    type = models.ManyToManyField(BetType)
    revised = models.BooleanField()

    def __str__(self):
        return self.name