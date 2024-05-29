from genres.models import Genres
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genres.serializers import genreSerializer

class genresCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genres.objects.all()
    serializer_class = genreSerializer


class genresRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genres.objects.all()
    serializer_class = genreSerializer