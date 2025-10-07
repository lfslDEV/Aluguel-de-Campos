from django.urls import path
from .views import busca_campos, solicitar_reserva, minhas_reservas, cancelar_reserva


urlpatterns = [
    path('', busca_campos, name='busca_campos'),
    path('reserva/<int:campo_id>/', solicitar_reserva, name='solicitar_reserva'),
    path('minhas_reservas/', minhas_reservas, name='minhas_reservas'),
    path('cancelar_reserva/<int:reserva_id>/', cancelar_reserva, name='cancelar_reserva'),
]