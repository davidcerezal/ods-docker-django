from django.db import models
from .bet import Bet
from .event import Event
import uuid


class ApiImporter(models.Model):
    api = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    counter = models.FloatField(blank=True)
    limit = models.FloatField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.api

    def is_exeded(self):
        return int(self.counter) >= int(self.limit)

    def add_attemp(self):
        self.counter = self.counter + 1
        self.save()
