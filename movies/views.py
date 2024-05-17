from rest_framework import generics
from movies.models import Movie
from movies.serializers import movieSerializer

class movieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = movieSerializer


class movieRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = movieSerializer
