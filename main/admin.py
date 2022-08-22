from django.contrib import admin
from .models import Movie_model, Review

admin.site.register(Movie_model)

admin.site.register(Review)