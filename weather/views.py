from django.views import generic


class WeatherHelloTemplateView(generic.TemplateView):
    template_name = "weather/weather_hello.html"
