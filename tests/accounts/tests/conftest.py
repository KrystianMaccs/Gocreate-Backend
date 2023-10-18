import pytest
from django.contrib.auth import get_user_model




User = get_user_model()

@pytest.fixture(autouse=True)
def user():
    return User.objects.create(
        username="testuser",
        first_name="John",
        last_name="Doe",
        email="test@example.com",
        is_artist=False,
        gender="MALE",
        is_staff=False,
        is_active=True,
    )

@pytest.fixture(autouse=True)
def artist_user():
    return User.objects.create(
        username="artistuser",
        first_name="Alice",
        last_name="Smith",
        email="artist@example.com",
        is_artist=True,
        gender="FEMALE",
        is_staff=False,
        is_active=True,
    )
