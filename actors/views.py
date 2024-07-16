from rest_framework import generics
from actors.models import Actors
from actors.serializers import actorsSerializers
from rest_framework.permissions import IsAuthenticated
from app.permissions import globalPermissions


class actorsCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Actors.objects.all()
    serializer_class = actorsSerializers


class actorsRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, globalPermissions)
    queryset = Actors.objects.all()
    serializer_class = actorsSerializers
