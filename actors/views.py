from rest_framework import generics
from actors.models import Actors
from actors.serializers import actorsSerializers


class actorsCreateListView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = actorsSerializers


class actorsRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = actorsSerializers
