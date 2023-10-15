from django.urls import path
from .views import ArtistUpdateView



urlpatterns = [
    path("artist/update/", ArtistUpdateView.as_view(), name="artist-update")
]
