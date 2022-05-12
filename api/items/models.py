from django.db import models

from core.models import BaseModel


class Item(BaseModel):
    name = models.CharField(max_length=32)
    base_price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=7, decimal_places=2)
    final_price = models.DecimalField(max_digits=7, decimal_places=2)
    
    def save(self, *args, **kwargs):
        if self.base_price:
            self.final_price = self.base_price * (1 + self.tax)
        else:
            self.final_price = self.base_price = 0
        super(Item, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
