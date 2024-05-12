from django.http import JsonResponse
from genres.models import Genres
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404

@csrf_exempt
def genres_create_list(request):
    if request.method == "GET":
        genres = Genres.objects.all()
        data = [{'id':genre.id, 'name':genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genres(name=data['name'])
        new_genre.save()
        return JsonResponse({'id':new_genre.id, 'name':new_genre.name}, status=201,)
    
@csrf_exempt
def genre_detail(request, pk):
    genre = get_object_or_404(Genres, pk=pk)

    if request.method == "GET":
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data)
    
    elif request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            {'id': genre.id, 'name':genre.name}
        )
    
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            {'message':'Gênero deletado com sucesso!'},
            status=204,
        )