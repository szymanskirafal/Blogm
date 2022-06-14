from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('weather.urls', namespace='weather')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/dj-rest-auth/facebook/', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
