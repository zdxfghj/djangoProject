
from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name="home"),
    path('film', views.film, name="film"),
    path('rating', views.rating,name="rating"),
    path('show/<movie_id>/', views.show,name="show"),
    path('contact', views.contact,name="contact"),
    path("addreview",views.add_review,name="addreview")
]
