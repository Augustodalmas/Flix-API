from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class movieAdmin(admin.ModelAdmin):
        list_display = ('id', 'title', 'releaseDate', 'resume')
