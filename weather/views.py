from django.shortcuts import get_object_or_404
from django.views import generic
from .models import City, WeatherInCity


class WeatherCitiesListView(generic.ListView):
    context_object_name = "cities"
    model = City
    template_name = "weather/weather_cities.html"


class WeatherInCityListView(generic.ListView):
    context_object_name = "weathers"
    model = WeatherInCity
    template_name = "weather/weather_in_city.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = self.city
        return context

    def get_queryset(self):
        self.city = get_object_or_404(City, pk=self.kwargs['city_id'])
        return WeatherInCity.objects.filter(city=self.city).order_by('-measurement_time')


class WeatherHelloTemplateView(generic.TemplateView):
    template_name = "weather/weather_hello.html"
