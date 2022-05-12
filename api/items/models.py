from django.db import models

from core.models import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=32)
    base_price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=7, decimal_places=2)
    final_price = models.DecimalField(max_digits=7, decimal_places=2)
    # Create a field to store the company name for each item. Think about the most ideal way. 
    
    def __str__(self):
        return self.name
