from celery import shared_task
from datetime import datetime
import os
import requests

from config import settings
from .models import City
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
        return True
    else:
        return False
