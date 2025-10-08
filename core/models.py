from django.db import models
from django.contrib.auth.models import User


class Campo(models.Model):
    nome_clube = models.CharField(max_length=100) 
    endereco = models.CharField(max_length=255) 
    cidade = models.CharField(max_length=100) 
    dimensao = models.CharField(max_length=50) 
    preco_por_hora = models.DecimalField(max_digits=6, decimal_places=2) 

    def __str_(self):
        return self.nome_clube
    
class Reserva(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE) 
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    dia = models.DateField() 
    horario_inicio = models.TimeField() 
    horario_termino = models.TimeField() 
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) 

    def __str__(self):
        return f"Reserva de {self.campo.nome_clube} para {self.usuario.username}"