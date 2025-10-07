from django.db import models
from django.contrib.auth.models import User

# configurando os modelos do banco.

class Campo(models.Model):
    nome_clube = models.CharField(max_length=100) # setar o nome do clube com o tamanho de 100 caracteres
    endereco = models.CharField(max_length=255) # setar o endereço com o tamanho de 255 caracteres
    cidade = models.CharField(max_length=100) # setar a cidade com o tamanho de 100 caracteres
    dimensao = models.CharField(max_length=50) # setar a dimensão com o tamanho de 50 caracteres
    preco_por_hora = models.DecimalField(max_digits=6, decimal_places=2) # setar o preço por hora com 6 dígitos no total e 2 casas decimais

    def __str_(self):
        return self.nome_clube
    
class Reserva(models.Model):
    campo = models.ForeignKey(Campo, on_delete=models.CASCADE) # relaciona a reserva com o campo, se o campo for deletado, a reserva também será deletada
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # relaciona a reserva com o usuário, se o usuário for deletado, a reserva também será deletada
    dia = models.DateField() # setar o dia da reserva
    horario_inicio = models.TimeField() # setar a hora de início da reserva
    horario_termino = models.TimeField() # setar a hora de fim da reserva
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True) # setar o valor total da reserva com 8 dígitos no total e 2 casas decimais, pode ser nulo ou em branco

    def __str__(self):
        return f"Reserva de {self.campo.nome_clube} para {self.usuario.username}"