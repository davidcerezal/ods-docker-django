from django.db import models


class BetModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    value = models.CharField(max_length=20)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return self.name
