from rest_framework import generics
from movies.models import Movie
from movies.serializers import movieModelSerializer, movieSerializer

class movieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = movieModelSerializer


class movieRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = movieModelSerializer
