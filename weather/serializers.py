from rest_framework import serializers
from .models import WeatherInCity


class WeatherInCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInCity
        fields = [
            "id",
            "city",
            "temp",
            "pressure",
            "humidity",
            "measurement_time",
            "source",
        ]
