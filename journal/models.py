from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Trade(models.Model):
    TRADE_TYPE = [
        ('BUY', 'Buy'),
        ('SELL', 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trade_type} {self.company} ({self.quantity} @ {self.price})"
