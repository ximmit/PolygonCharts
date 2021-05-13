from django.db import models

# Create your models here.

class HistoricalData(models.Model):
    ticker = models.TextField()
    o = models.TextField()
    h = models.TextField()
    l = models.TextField()
    c = models.TextField()
    v_name = models.TextField()
    vw = models.TextField()
    t = models.TextField()
    n = models.TextField()
    def __str__(self):
        return self.t
