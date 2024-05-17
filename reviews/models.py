from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'O valor de avaliação não pode ser inferior a 0 estrelas!'),
            MaxValueValidator(5, 'O valor de avaliação não pode ser superior a 5 estrelas!'),
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.movie
