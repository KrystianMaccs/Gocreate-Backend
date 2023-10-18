import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import Artist
from gocreate.settings.base import AUTH_USER_MODEL


logger = logging.getLogger(__name__)



@receiver(post_save, sender=AUTH_USER_MODEL)
def create_artist_profile(sender, instance, created, **kwargs):
    if created and instance.is_artist:
        Artist.objects.create(user=instance)
        logger.info(f"{instance}'s profile created")
        print("Artist has been created")


        