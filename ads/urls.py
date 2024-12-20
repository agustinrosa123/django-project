# ads/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views  # Si vas a usar LoginView de Django

from . import views  # Asegúrate de importar las vistas de tu aplicación

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página de inicio
    path('ads/', views.ads_list, name='ads_list'),  # Ruta para la lista de anuncios
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Ruta para el login
]
