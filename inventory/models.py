# inventory/models.py
from django.db import models

class Inventory(models.Model):
    stock_name = models.CharField(max_length=100)
    stock_type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    warehouse_location = models.CharField(max_length=100)
    availability_status = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.stock_name} - {self.warehouse_location}"