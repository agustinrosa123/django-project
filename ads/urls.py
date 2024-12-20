from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.ads_list, name='ads_list'),  # Asegúrate de que 'views.ads_list' esté correcto
]
