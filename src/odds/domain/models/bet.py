from datetime import datetime
from django.utils import timezone
from django.db import models
from .betMarket import BetMarket
from .betType import BetType
import uuid


class Bet(models.Model):
    name = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255, blank=True, unique=True, default=uuid.uuid4)
    price = models.FloatField(blank=True)
    value = models.CharField(max_length=20, blank=True)
    expiry_date = models.DateTimeField()
    contra_bet = models.ManyToManyField('self', blank=True)
    market = models.ManyToManyField(BetMarket, blank=True)
    type = models.ManyToManyField(BetType)
    revised = models.BooleanField()

    def __str__(self):
        return self.name

    def get_event(self):
        return self.event_set.all()

    def updatePrice(self, price):
        self.price =price
        self.revised = False
        self.save()

    def isExpired(self):
        return True if self.expiry_date < timezone.now() else False