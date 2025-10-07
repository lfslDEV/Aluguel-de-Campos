from django.urls import path
from .views import busca_campos, solicitar_reserva, minhas_reservas


urlpatterns = [
    path('', busca_campos, name='busca_campos'),
    path('reserva/<int:campo_id>/', solicitar_reserva, name='solicitar_reserva'),
    path('minhas_reservas/', minhas_reservas, name='minhas_reservas'),
]