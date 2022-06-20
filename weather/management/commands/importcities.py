import csv
import sys
from django.core.management import BaseCommand

from weather.models import City, Voivodeship


class Command(BaseCommand):
    help = 'Load a cities csv file into the database'

    def handle(self, *args, **kwargs):
        with open('weather/cities.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            cities = [
                City(
                    name = row[0],
                    voivodeship = Voivodeship.objects.get(name__iexact=row[4])
                )
                for row in csv_reader
                if row[1] == 'miasto'
            ]
        City.objects.bulk_create(cities)
