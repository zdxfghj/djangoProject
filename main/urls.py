
from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name="home"),
    path('film', views.film, name="film"),
    path('rating', views.rating,name="rating"),
    path('show', views.show,name="show"),
    path('contact', views.contact,name="contact"),
]
