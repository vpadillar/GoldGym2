from django.http import HttpResponse
# Create your views here.

def login(request):
    return HttpResponse("Hola mundo - Este es mi login.")
