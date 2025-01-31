from django.urls import path
from . import views  # Asegúrate de que la importación sea correcta

urlpatterns = [
    path('saludo/', views.saludo),  # La URL debe coincidir con el patrón
]
