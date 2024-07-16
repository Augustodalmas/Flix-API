from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import movieModelSerializer
from app.permissions import globalPermissions

class movieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Movie.objects.all()
    serializer_class = movieModelSerializer


class movieRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Movie.objects.all()
    serializer_class = movieModelSerializer
