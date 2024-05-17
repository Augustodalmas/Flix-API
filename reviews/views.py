from rest_framework import generics
from reviews.models import Review
from reviews.serializers import reviewSerializer

class reviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = reviewSerializer


class reviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = reviewSerializer