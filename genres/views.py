from genres.models import Genres
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.serializers import genreSerializer
from app.permissions import globalPermissions

class genresCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Genres.objects.all()
    serializer_class = genreSerializer


class genresRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Genres.objects.all()
    serializer_class = genreSerializer