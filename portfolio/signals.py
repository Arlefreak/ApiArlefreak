from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Project

@receiver(post_save, sender=Project)
def init_new_project(sender, instance, signal, created, **kwargs):
    if created:
        pass
        # instance.top()
