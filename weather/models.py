from django.db import models


class Voivodeship(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    name = models.CharField(max_length=50)
    voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'voivodeship'],
                name='unique city in voivodeship',
            )
        ]
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name}"


class WeatherInCity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temp = models.SmallIntegerField()
    pressure = models.PositiveSmallIntegerField()
    humidity = models.PositiveSmallIntegerField()
    measurement_time = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=50)
    weather_type = models.CharField(blank=True, max_length=50)

    class Meta:
        verbose_name_plural = "Weather in the City"

    def __str__(self):
        return f"{self.city.name} - {self.temp} / {self.measurement_time}"
