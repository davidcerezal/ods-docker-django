from django.db import models


class BetType(models.Model):
    name = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255, blank=True, default='')
    description = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

