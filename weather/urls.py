from django.urls import path

from .views import (
    WeatherAboutTemplateView,
    WeatherCitiesListView,
    WeatherInCityListView,
    WeatherHelloTemplateView,
    WeatherVoivodeshipsListView,)

app_name = 'weather'
urlpatterns = [
    path("", WeatherHelloTemplateView.as_view(), name="weather-hello"),
    path("about/", WeatherAboutTemplateView.as_view(), name="weather-about"),
    path(
        "voivodeships/",
        WeatherVoivodeshipsListView.as_view(),
        name="weather-voivodeships"),
    path(
        "voivodeships/<int:voivodeship_id>/cities/",
        WeatherCitiesListView.as_view(),
        name="weather-cities"),
    path(
        "voivodeships/<int:voivodeship_id>/cities/<int:city_id>/",
        WeatherInCityListView.as_view(),
        name="weather-in-city"),
]
