from django.db import models
from genres.models import Genres
from actors.models import Actors


class Movie(models.Model):
    title = models.CharField(max_length=256)
    genre = models.ForeignKey(Genres, on_delete=models.PROTECT, related_name='movies')
    releaseDate = models.DateField(blank=True, null=True)
    actors = models.ManyToManyField(Actors, related_name='movies')
    resume = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
