from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola Django - Coder!")  # Asegúrate de que el texto esté entre comillas
