from django_countries.serializer_fields import CountryField
from rest_framework import fields, serializers

from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    is_artist = serializers.BooleanField(source="user.is_artist")
    full_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    
    class Meta:
        model = Artist
        fields = [
            "username",
            "first_name",
            "last_name",
            "full_name",
            "stage_name",
            "is_artist",
            "email",
            "id",
            "phone_number",
            "bio",
            "gender",
            "country",
            "country_code",
            "city",
            "music_class",
            "company_name",
            "sor",
            "lga",
            "address",
            "postal_code",
            "state",
            "city",
            "dob",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Artist
        fields = [
            "phone_number",
            "bio",
            "gender",
            "country",
            "city",
            "music_class",
            "company_name",
            "address",
        ]