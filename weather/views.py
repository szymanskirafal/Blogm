from django.shortcuts import get_object_or_404
from django.views import generic
from .models import City, Voivodeship, WeatherInCity


class WeatherCitiesListView(generic.ListView):
    context_object_name = "cities"
    model = City
    template_name = "weather/weather_cities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voivodeship'] = self.voivodeship
        return context

    def get_queryset(self):
        self.voivodeship = get_object_or_404(Voivodeship, pk=self.kwargs['voivodeship_id'])
        return City.objects.filter(voivodeship=self.voivodeship).order_by('name')


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


class WeatherAboutTemplateView(generic.TemplateView):
    template_name = "weather/weather_about.html"


class WeatherHelloTemplateView(generic.TemplateView):
    template_name = "weather/weather_hello.html"


class WeatherVoivodeshipsListView(generic.ListView):
    context_object_name = 'voivodeships'
    model = Voivodeship
    template_name = "weather/weather_voivodeships.html"
