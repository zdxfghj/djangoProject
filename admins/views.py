
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from main.models import Movie_model,Review
from django.urls import reverse


def index(request):

    return render(request, 'admins/index.html',)

