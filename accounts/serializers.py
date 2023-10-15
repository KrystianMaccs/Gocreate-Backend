from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from djoser.serializers import UserCreateSerializer
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="artist.gender")
    phone_number = PhoneNumberField(source="artist.phone_number")
    country = CountryField(source="artist.country")
    city = serializers.CharField(source="artist.city")
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    is_artist = serializers.BooleanField()
    dob = serializers.CharField(source="artist.bio")
    bio = serializers.CharField(source="artist.bio")
    sor = serializers.CharField(source="artist.sor")
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "is_artist",
            "gender",
            "phone_number",
            "country",
            "city",
            "dob",
            "bio",
            "sor",
            
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CreateUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_artist", "password"]
