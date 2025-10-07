from django.urls import path
from . import views
from .views import busca_campos, solicitar_reserva, minhas_reservas


urlpatterns = [
    path('', views.busca_campos, name='login'),
    path('busca/', busca_campos, name='busca_campos'),
    path('reserva/<int:campo_id>/', solicitar_reserva, name='solicitar_reserva'),
    path('minhas_reservas/', minhas_reservas, name='minhas_reservas'),
]