from django.db import models
from .betMarket import BetMarket


class ImportResult(models.Model):
    name = models.CharField(max_length=255)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    status = models.CharField(max_length=20)
    market = models.ForeignKey(BetMarket, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
