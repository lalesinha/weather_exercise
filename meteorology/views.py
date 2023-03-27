from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import WeatherStation, WeatherData
from .serializers import WeatherStationSerializer, WeatherDataSerializer


def hello(request):
    data = {
        'message': 'Hello, World!'
    }
    return JsonResponse(data)

@api_view(['GET'])
def get_all_weather_stations(request):
    weather_stations = WeatherStation.objects.all()
    serializer = WeatherStationSerializer(weather_stations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_single_weather_station(request, station_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    serializer = WeatherStationSerializer(weather_station)
    return Response(serializer.data)

@api_view(['PUT'])
def update_weather_station(request, station_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    serializer = WeatherStationSerializer(weather_station, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_weather_station(request, station_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    weather_station.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_weather_data(request, station_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    serializer = WeatherDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(station=weather_station)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_all_weather_data_for_station(request, station_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    weather_data = WeatherData.objects.filter(station=weather_station)
    serializer = WeatherDataSerializer(weather_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_single_weather_data(request, station_id, data_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    weather_data = get_object_or_404(WeatherData, pk=data_id, station=weather_station)
    serializer = WeatherDataSerializer(weather_data)
    return Response(serializer.data)

@api_view(['PUT'])
def update_weather_data(request, station_id, data_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    weather_data = get_object_or_404(WeatherData, pk=data_id, station=weather_station)
    serializer = WeatherDataSerializer(weather_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_weather_data(request, station_id, data_id):
    weather_station = get_object_or_404(WeatherStation, pk=station_id)
    weather_data = get_object_or_404(WeatherData, pk=data_id, station=weather_station)
    weather_data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)