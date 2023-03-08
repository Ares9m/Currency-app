from django.db import models

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=30)
    symbol = models.CharField(max_length=3, unique=True)
    exchange_rate = models.FloatField()

    def __str__(self):
        return self.name + ' ' + self.symbol