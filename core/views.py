
from django.shortcuts import render, get_object_or_404, redirect
from .models import Campo, Reserva
from django.contrib.auth.decorators import login_required
from datetime import datetime
from decimal import Decimal

def busca_campos(request):
    cidade = request.GET.get('cidade')
    campos = None
    if cidade:
        campos = Campo.objects.filter(cidade__icontains=cidade)
    return render(request, 'core/busca_campos.html', {'campos': campos})

@login_required
def solicitar_reserva(request, campo_id):
    campo = get_object_or_404(Campo, id=campo_id)

    if request.method == 'POST':
        dia = request.POST.get('dia')
        horario_inicio_str = request.POST.get('horario_inicio')
        horario_termino_str = request.POST.get('horario_termino')
        horario_inicio = datetime.strptime(horario_inicio_str, '%H:%M').time()
        horario_termino = datetime.strptime(horario_termino_str, '%H:%M').time()
        duracao_em_horas = (datetime.combine(datetime.min, horario_termino) - datetime.combine(datetime.min, horario_inicio)).seconds / 3600
        valor_total_calculado = Decimal(duracao_em_horas) * campo.preco_por_hora

        reserva = Reserva(
            campo=campo,
            usuario=request.user,
            dia=dia,
            horario_inicio=horario_inicio,
            horario_termino=horario_termino,
            valor_total=valor_total_calculado
        )
        reserva.save()

        return redirect('minhas_reservas')

    context = {
        'campo': campo
    }
    return render(request, 'core/solicitar_reserva.html', context)

@login_required 
def minhas_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user).order_by('dia', 'horario_inicio')

    context = {
        'reservas': reservas
    }
    return render(request, 'core/minhas_reservas.html', context)