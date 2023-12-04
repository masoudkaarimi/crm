from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver

from .models import Customer


# Must be import signals to apps.py and set apps.py to settings.py or __init__.py

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(user=instance, name=instance.username)
        print("[INFO] - Customer Profile Created.")

# post_save.connect(create_customer_profile, sender=User)
