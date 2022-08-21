from django.shortcuts import render
from .models import Movie_model


def index(request):
    return render(request, 'main/index.html')


def film(request):
    Movie = Movie_model.objects.all()
    return render(request, 'main/films.html',{'title':'Фильмы','movie': Movie})


def rating(request):
    return render(request, 'main/rating.html')


def show(request):
    Movie = Movie_model.objects.all()
    return render(request, 'main/show.html',{'title':'Главная','movie': Movie})


def contact(request):
    return render(request, 'main/contact.html')
