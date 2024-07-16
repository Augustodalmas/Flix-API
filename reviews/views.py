from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializers import reviewSerializer
from app.permissions import globalPermissions

class reviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Review.objects.all()
    serializer_class = reviewSerializer


class reviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Review.objects.all()
    serializer_class = reviewSerializer