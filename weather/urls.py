from django.urls import path

from .views import WeatherCitiesListView, WeatherInCityListView, WeatherHelloTemplateView

app_name = 'weather'
urlpatterns = [
    path("", WeatherHelloTemplateView.as_view(), name="weather-hello"),
    path("cities/", WeatherCitiesListView.as_view(), name="weather-cities"),
    path("cities/<int:city_id>/", WeatherInCityListView.as_view(), name="weather-in-city"),
]
