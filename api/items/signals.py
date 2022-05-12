from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Item
 
 
@receiver(post_save, sender=Item)
def create_instance(sender, instance, created, **kwargs):
    if created:
        actual_final_price = instance.base_price * (1 + instance.tax)
        instance.final_price = actual_final_price

@receiver(post_save, sender=Item)
def save_profile(sender, instance, **kwargs):
        actual_final_price = instance.base_price * (1 + instance.tax)
        instance.final_price = actual_final_price