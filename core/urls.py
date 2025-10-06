from django.urls import path
from . import views

urlpatterns = [
    path('busca/', views.busca_campos, name='busca_campos'),
    path('reserva/<int:campo_id>/', views.solicitar_reserva, name='solicitar_reserva'),
]