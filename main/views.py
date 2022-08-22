from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Movie_model, Review
from django.urls import reverse


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
    movie.visit_count +=1
    movie.save()
    revier_list = movie.review_set.all().order_by("-date")

    print(movie.review_set.all())
    return render(request, 'main/show.html',{'movie': movie,"revier_list":revier_list})


def contact(request):
    return render(request, 'main/contact.html')


def add_review(request):
    print(request.POST)
    movie = Movie_model.objects.get(pk=request.POST["movie"])
    review = Review(name_user=request.POST['review_name'], description=request.POST["review_text"], movie=movie)
    review.save()
    return HttpResponseRedirect(reverse('main:show', args=[request.POST["movie"]]))
