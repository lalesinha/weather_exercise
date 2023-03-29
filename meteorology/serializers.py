from rest_framework import serializers
from .models import WeatherStation
from .models import WeatherData

class WeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStation
        fields = '__all__'

class WeatherStationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStation
        fields = ('name',) 

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'
    

        