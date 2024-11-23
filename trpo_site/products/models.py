from django.db import models
from django.utils import timezone

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30, default="Без категории")
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    incoming_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
