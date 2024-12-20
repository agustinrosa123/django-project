from django.shortcuts import render

def listado_anuncios(request):
    # Puedes pasar un contexto aquí si lo necesitas
    return render(request, 'ads/listado_anuncios.html')
