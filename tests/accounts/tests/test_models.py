import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import Gender

User = get_user_model()



@pytest.mark.django_db
def test_user_get_full_name(user):
    full_name = user.get_full_name
    assert full_name == "John Doe"

@pytest.mark.django_db
def test_artist_user_get_full_name(artist_user):
    full_name = artist_user.get_full_name
    assert full_name == "Alice Smith"

