from django.db import models

# Create your models here.
class Symbol(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=100, default='DIGITAL_CURRENCY_DAILY')
    market = models.CharField(max_length=10, blank=True)
    close = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    precent = models.FloatField(default=0.0)
    delta = models.FloatField(default=0.0)

    def __str__(self):
        return '%s' % self.name
