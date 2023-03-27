from django.contrib.gis.db import models

class WeatherStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()

    class Meta:
        db_table = "weather_stations"
        managed = False

class WeatherData(models.Model):
    station_id = models.ForeignKey(WeatherStation, on_delete=models.CASCADE, db_column='station_id')
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = "weather_data"
        managed = False
       