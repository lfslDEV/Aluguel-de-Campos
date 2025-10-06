from django.shortcuts import render, redirect
from .models import Campo, Reserva
from django.contrib.auth.decorators import login_required

def busca_campos(request): 
    cidade = request.GET.get('cidade') 
    campos = None 
    if cidade:
        campos = Campo.objects.filter(cidade__icontains=cidade)
    return render(request, 'core/busca_campos.html', {'campos': campos})

@login_required
def solicitar_reserva(request, campo_id):  
    campo = Campo.objects.get(id=campo_id) 
    if request.method == 'POST':
        return redirect('minhas_reservas') 
    return render(request, 'core/solicitar_reserva.html', {'campo': campo}) 
