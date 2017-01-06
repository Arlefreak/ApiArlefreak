from .models import Link
from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=Link)
# def save_name(sender, instance, **kwargs):
#     # if kwargs.get('created', False):
#     obj=kwargs['instance']
#     UserProfile.objects.get_or_create(user=kwargs.get('instance'))
