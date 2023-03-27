from django.urls import path
from . import views


urlpatterns = [
    path('weather_stations/all/', views.get_all_weather_stations, name='get_all_weather_stations'),
    path('weather_stations/<int:station_id>/', views.get_single_weather_station, name='get_single_weather_station'),
    path('weather_stations/<int:station_id>/update/', views.update_weather_station, name='update_weather_station'),
    path('weather_stations/<int:station_id>/delete/', views.delete_weather_station, name='delete_weather_station'),
    path('weather_stations/<int:station_id>/weather_data/', views.create_weather_data, name='create_weather_data'),
    path('weather_stations/<int:station_id>/weather_data/all/', views.get_all_weather_data_for_station, name='get_all_weather_data_for_station'),
    path('weather_stations/<int:station_id>/weather_data/<int:data_id>/', views.get_single_weather_data, name='get_single_weather_data'),
    path('weather_stations/<int:station_id>/weather_data/<int:data_id>/update/', views.update_weather_data, name='update_weather_data'),
    path('weather_stations/<int:station_id>/weather_data/<int:data_id>/delete/', views.delete_weather_data, name='delete_weather_data'),
]