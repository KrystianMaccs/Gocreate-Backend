from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .permissions import IsArtistPermission
from .models import Artist
from .serializers import ArtistSerializer

class ArtistUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsArtistPermission]

    def get(self, request, format=None):
        user = self.request.user
        if user.is_artist:
            artist, created = Artist.objects.get_or_create(user=user)
            serializer = ArtistSerializer(artist)
            return Response(serializer.data)
        else:
            raise PermissionDenied("You must set 'is_artist' to 'True' to update your profile.")

    def put(self, request, format=None):
        user = self.request.user
        if user.is_artist:
            artist, created = Artist.objects.get_or_create(user=user)
            serializer = ArtistSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionDenied("You must set 'is_artist' to 'True' to update your profile.")