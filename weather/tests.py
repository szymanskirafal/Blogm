from config import settings
import pytest
import requests



class TestOpenWeather:
    def test_appid(self):
        appid_expected = '0db462d7cd3cd90563fd7059cbe2a4f5'
        appid_given = settings.APPID
        assert appid_expected == appid_given

    def test_url(self):
        url_expected = "https://api.openweathermap.org/data/2.5/weather?q=Zielona Gora&appid=0db462d7cd3cd90563fd7059cbe2a4f5&units=metric"
        appid = settings.APPID
        city_name = 'Zielona Gora'
        url_given = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}&units=metric"
        assert url_expected == url_given

    def test_response(self):
        url_expected = "https://api.openweathermap.org/data/2.5/weather?q=Zielona Gora&appid=0db462d7cd3cd90563fd7059cbe2a4f5&units=metric"
        appid = settings.APPID
        city_name = 'Zielona Gora'
        url_given = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}&units=metric"
        response_expected = requests.get(url_expected)
        response_expected = response_expected.json()
        response_given = requests.get(url_given)
        response_given = response_given.json()
        assert response_expected == response_given
