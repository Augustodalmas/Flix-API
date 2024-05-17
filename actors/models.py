from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BR', 'Brasil'),
)

class Actors(models.Model):
    name = models.CharField(max_length=256)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=256, choices=NATIONALITY_CHOICES)

    def __str__(self) -> str:
        return self.name
