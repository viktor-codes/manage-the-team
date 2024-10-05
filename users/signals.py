# In users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from team_manager_api.models import Employee


@receiver(post_save, sender=CustomUser)
def create_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
