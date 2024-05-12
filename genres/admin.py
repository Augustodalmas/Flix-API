from django.contrib import admin
from genres.models import Genres

@admin.register(Genres)
class adminGenres(admin.ModelAdmin):
    list_display = ('id', 'name')
