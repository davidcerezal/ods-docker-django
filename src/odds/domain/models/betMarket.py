from django.db import models


class BetMarket(models.Model):
    name = models.CharField(max_length=255)
    alias = models.TextField(default='')
    url = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255, blank=True)
    api_pass = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

    def add_alias(self, alias):
        self.alias = self.alias + ', ' + alias
