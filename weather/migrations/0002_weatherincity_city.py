# Generated by Django 4.0.5 on 2022-06-13 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherincity',
            name='city',
            field=models.ForeignKey(default=11111111111, on_delete=django.db.models.deletion.CASCADE, to='weather.city'),
            preserve_default=False,
        ),
    ]
