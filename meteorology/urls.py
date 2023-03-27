from django.urls import path
from . import views


urlpatterns = [
    path('station/', views.get_all_weather_stations),
    path('station/', views.get_weather_station),
    path('station/', views.create_weather_station),
    path('station/', views.update_weather_station),
    path('station/', views.delete_weather_station),
    path('station/', views.get_all_weather_data),
    path('station/', views.get_weather_data),
    path('station/', views.create_weather_data),
    path('station/', views.update_weather_data),
    path('station/', views.delete_weather_data),
   
]