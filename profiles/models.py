#from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from gocreate.settings.base import AUTH_USER_MODEL

from common.models import TimeStampedUUIDModel

# User = get_user_model()
User = AUTH_USER_MODEL


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Artist(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="artist", on_delete=models.CASCADE)
    stage_name = models.CharField(verbose_name=_("Stage Name"), max_length=255, unique=True)
    gender = models.CharField(verbose_name=_("Gender"), choices=Gender.choices, default=Gender.OTHER, max_length=20)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+2348037286666", unique=True)
    bio = models.CharField(verbose_name=_("Bio"), max_length=255, blank=True, null=True)
    music_class = models.CharField(verbose_name=_("Music Class"), max_length=255, blank=True)
    company_name = models.CharField(verbose_name=_("Company Name"), max_length=55, blank=True)
    sor = models.CharField(verbose_name=_("State of Residence"), max_length=255, blank=True)
    lga = models.CharField(verbose_name=_("Local Government Area"), max_length=225, blank=True, null=True)
    address = models.CharField(verbose_name=_("Address"), blank=True, max_length=225)
    postal_code = models.CharField(verbose_name=_("Postal Code"), blank=True, null=True, max_length=8)
    country = CountryField(verbose_name=_("Country"), default="NG", blank=True, null=True)
    country_code = models.CharField(verbose_name=_('Country Code'), default="NG", blank=True, max_length=5) 
    state = models.CharField(verbose_name=_("State"), max_length=25, null=True, blank=True) 
    city = models.CharField(verbose_name=_("city"), max_length=75, null=True, blank=True) 
    dob = models.DateField(verbose_name=_("Date of Birth"), null=True)
    
    
    def __str__(self):
        return f"{self.user.username}'s profile"