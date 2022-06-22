from celery import shared_task
from datetime import datetime
import os
import requests

from config import settings
from django.db.models import Avg
from .models import City, Voivodeship, WeatherInCity, WeatherInVoivodeship
from .serializers import WeatherInCitySerializer


@shared_task
def check_weather():
    data_for_all_cities = []
    cities = City.objects.all()
    cities = cities.filter(voivodeship__name__iexact='lubuskie')
    appid = '0db462d7cd3cd90563fd7059cbe2a4f5'
    for city in cities:
        if city.name == 'Zielona Góra':
            city_name = 'Zielona Gora'
        else:
            city_name = city.name
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}&units=metric"
        response = requests.get(url)
        response = response.json()
        weather = response['main']
        data_for_city = {
            'city' : city.pk,
            'temp': int(weather['temp']),
            'pressure': int(weather['pressure']),
            'humidity': int(weather['humidity']),
            'measurement_time': datetime.now(),
            'source': 'OpenWeatherMap',}
        data_for_all_cities.append(data_for_city)
    serializer = WeatherInCitySerializer(data=data_for_all_cities, many=True)
    if serializer.is_valid():
        serializer.save()
        calculate_and_save_weather_for_voivodeship.delay()
        return True
    else:
        return False

@shared_task
def calculate_and_save_weather_for_voivodeship():
    cities = City.objects.all()
    cities = cities.filter(voivodeship__name__iexact='lubuskie')
    nr_of_cities_in_voivodeship = cities.count()

    weather_in_cities = WeatherInCity.objects.filter(city__in=cities)
    weather_in_cities = weather_in_cities.order_by('-measurement_time')
    weather_in_cities = weather_in_cities[:nr_of_cities_in_voivodeship]
    weather_in_cities = weather_in_cities.aggregate(
        average_temp=Avg('temp'),
        average_pressure=Avg('pressure'),
        average_humidity=Avg('humidity'),
        )
    WeatherInVoivodeship.objects.create(
        voivodeship = Voivodeship.objects.get(name='Lubuskie'),
        temp = int(weather_in_cities['average_temp']),
        pressure = int(weather_in_cities['average_pressure']),
        humidity = int(weather_in_cities['average_humidity']),
        measurement_time = datetime.now(),
        )
    return True
