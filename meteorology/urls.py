from django.urls import path
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.get_all_weather_stations),
]