from django.urls import path

from .views import FacebookLogin


urlpatterns = [
    path("", FacebookLogin.as_view(), name="facebook-login"),
]
