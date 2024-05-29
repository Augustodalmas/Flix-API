from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genres
from actors.models import  Actors


class movieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        reviews = obj.reviews.all()
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if reviews:
            return round(rate, 2)
        return None
    
    
    def validate_releaseDate(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("O ano de lançamento é menor que 1990.")
        return value
    

    def validate_resume(self, value):
        if len(value) > 250:
            raise serializers.ValidationError("O resumo não pode ter mais de 250 caracteres.")
        return value
        