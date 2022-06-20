# Generated by Django 4.0.5 on 2022-06-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_alter_city_name'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='city',
            constraint=models.UniqueConstraint(fields=('name', 'voivodeship'), name='unique city in voivodeship'),
        ),
    ]
