# Generated by Django 4.0.5 on 2022-06-14 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_voivodeship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='voivodeship',
        ),
    ]