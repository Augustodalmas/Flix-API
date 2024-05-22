from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from genres.models import Genres
from actors.models import  Actors

#Serializer de forma manual, sem usar o model para a criação do mesmo, dessa forma precisamos importar todos os models;
class movieSerializer(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genres.objects.all(),
        )
    releaseDate = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actors.objects.all(), 
        many=True,
        )
    resume = serializers.CharField()
    #Com esse serializar, não podemos usar o metodo create;""

#Serializer de forma automatica, dessa forma só precisamos do nosso model principal;
class movieModelSerializer(serializers.ModelSerializer):
    ratio = serializers.SerializerMethodField(read_only=True)

    class Meta():
        model = Movie
        fields = '__all__'

    def get_ratio(self, obj):
        #Método mais complexo
        reviews = obj.reviews.all()
        """
        if reviews:
            sum_ratio = 0
            for review in reviews:
                sum_ratio += review.stars
            reviewCount = obj.reviews.count()
            return round(sum_ratio / reviewCount, 1)
        return None
        """

        #Método Prático
        ratio = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if reviews:
            return round(ratio, 2)
        return None
    def validate_releaseDate(self, value):
        if value.year < 1990:
            raise serializers.ValidationError("O ano de lançamento é menor que 1990.")
        return value
    

    def validate_resume(self, value):
        if len(value) > 250:
            raise serializers.ValidationError("O resumo não pode ter mais de 250 caracteres.")
        return value
        