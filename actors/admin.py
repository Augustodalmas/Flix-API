from django.contrib import admin
from actors.models import Actors

@admin.register(Actors)
class actorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')