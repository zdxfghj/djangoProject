from django.shortcuts import render
from .models import Movie_model


def index(request):
    movie_list = Movie_model.objects.all()
    return render(request, 'main/index.html', {'movie_list': movie_list})


def film(request):
    movie_list = Movie_model.objects.all()
    return render(request, 'main/films.html',{'title':'Фильмы','movie_list': movie_list})


def rating(request):
    return render(request, 'main/rating.html')


def show(request, movie_id):
    movie = Movie_model.objects.get(pk=movie_id)
    return render(request, 'main/show.html',{'movie': movie})


def contact(request):
    return render(request, 'main/contact.html')
