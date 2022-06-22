from django.contrib import admin
from .models import City, Voivodeship, WeatherInCity, WeatherInVoivodeship

admin.site.register(City)
admin.site.register(Voivodeship)
admin.site.register(WeatherInCity)
admin.site.register(WeatherInVoivodeship)
