from django.shortcuts import render
from .models import Ad  # Suponiendo que tienes un modelo llamado Ad

# Vista para la lista de anuncios
def ads_list(request):
    ads = Ad.objects.all()  # Obtiene todos los anuncios de la base de datos
    return render(request, 'ads/ads_list.html', {'ads': ads})  # Renderiza la plantilla ads_list.html con los anuncios

# Vista para la página de inicio
def index(request):
    return render(request, 'ads/index.html')  # Renderiza la plantilla index.html
