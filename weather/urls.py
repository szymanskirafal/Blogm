from django.urls import path

from .views import WeatherHelloTemplateView


urlpatterns = [
    path("", WeatherHelloTemplateView.as_view(), name="weather-hello"),
]
