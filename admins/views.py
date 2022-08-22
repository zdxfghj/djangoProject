
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from main.models import Movie_model,Review
from django.urls import reverse


def index(request):
    movie_list = Movie_model.objects.all()
    return render(request, 'admins/index.html',{'movie_list': movie_list})

def update(request, movie_id):
    movie = Movie_model.objects.get(pk=movie_id)
    return render(request, 'admins/update.html',{'movie': movie})

