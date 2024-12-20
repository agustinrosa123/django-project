from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, esta es la página de inicio de Ads.")
