from django.shortcuts import render

# Vista para mostrar la lista de anuncios
def ads_list(request):
    # Aquí puedes obtener los anuncios desde la base de datos
    # y pasarlos al template.
    return render(request, 'ads/ads_list.html')  # Asegúrate de tener el template ads_list.html
