from django.db import models


class BetMarket(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    api_pass = models.CharField(max_length=255)

    def __str__(self):
        return self.name

