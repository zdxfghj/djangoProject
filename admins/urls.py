
from django.urls import path
from admins import views

app_name = 'admins'
urlpatterns = [
        path('', views.index, name="home"),
]
