from django.db import models

class PreMarketGainer(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20)
    change = models.CharField(max_length=20)
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticker}: {self.change}"
