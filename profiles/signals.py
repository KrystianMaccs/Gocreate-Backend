import logging

from django.db import transaction
from django.dispatch import receiver

from profiles.models import Artist

logger = logging.getLogger(__name__)

from djoser.signals import user_registered


@transaction.atomic
@receiver(user_registered)
def my_handler(user, request, **kwargs):
    logger.info(f"{user} has registered")
    artist = Artist.objects.create(user=user)
    logger.info(f"{artist} has been created")
