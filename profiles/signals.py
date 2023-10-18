import logging

from django.db import transaction
from django.dispatch import receiver

from profiles.models import Artist

from djoser.signals import user_registered
logger = logging.getLogger(__name__)



@transaction.atomic
@receiver(user_registered)
def my_handler(user, request, **kwargs):
    if user.is_artist:
        logger.info(f"{user} is an artist!")
        artist = Artist.objects.create(user=user)
        logger.info(f"{artist} has been created")
    else:
        logger.info(f"{user} is not an artist")
    