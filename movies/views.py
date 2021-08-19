import json

from django.http import JsonResponse
from django.views import View

from movies.models import Movie, Actor

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        result=[]
        for actor in actors:
            result.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "movie" : list(actor.movie_set.values("title"))
                }
            )
        return JsonResponse({'result': result},status=200)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        result=[]
        for movie in movies:
            result.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time, 
                    "first_name" : list(movie.actor.values("first_name"))
                }
            )
        return JsonResponse({'result': result},status=200)
