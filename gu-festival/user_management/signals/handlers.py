from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group
from user_management.models import UserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, created, **kwargs):
    if created:
        g = Group.objects.get(name='Musician')
        instance.groups.add(g)
        UserProfile.objects.create(user=instance)