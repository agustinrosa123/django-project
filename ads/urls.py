from django.urls import path
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django
from . import views  # Asegúrate de importar views para usar las vistas propias

urlpatterns = [
    path('ads/', views.ads_list, name='ads_list'),  # Ruta para la lista de anuncios
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Ruta para el login
]
