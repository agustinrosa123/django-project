# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', include('ads.urls')),  # Ruta para la aplicación de anuncios
    path('', include('ads.urls')),  # Ruta principal que redirige a la app ads
]
