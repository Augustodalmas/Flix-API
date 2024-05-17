from rest_framework import serializers
from actors.models import Actors

class actorsSerializers(serializers.ModelSerializer):

    class Meta():
        model = Actors
        fields = '__all__'