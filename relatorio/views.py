from django.shortcuts import render
from django.http import JsonResponse
from django.db import DatabaseError
import json
from atendimento.models import Atendimento
from user.models import Atendente, Veterinario, Cliente
from pet.models import Pet
from servico.models import Servico
from produto.models import Produto
from django.db.models import Sum

def index(request):
    veterinarios = Veterinario.objects.all()
    atendentes = Atendente.objects.all()
    clientes = Cliente.objects.all()
    return render(request,'relatorios.html', { 'veterinarios': veterinarios, 'atendentes': atendentes, 'clientes': clientes }) 

def relServicoProfissional(request, id = None, ano = None, mes = None):
    if Atendente.objects.filter(user_id = id).count() > 0:
        profissional = Atendente.objects.get(user_id = id)
    else:
        profissional = Veterinario.objects.get(user_id = id)
    
    print(profissional.user_id)
    itens = Atendimento.objects.filter(dataAtendimento__year=ano, dataAtendimento__month=mes, profissional_id = profissional.user_id).values('dataAtendimento', 'servico_id__descricao', 'status', 'cliente__nome', 'pet_id__nome', 'pet_id__tipo').order_by('-dataAtendimento') 
    return JsonResponse({'itens' : list(itens)})

def relServicoCliente(request, id = None, ano = None, mes = None):
    total = Atendimento.objects.filter(dataAtendimento__year=ano, dataAtendimento__month=mes, cliente_id = id).aggregate(Sum('servico_id__pataz__qtdPontos')) 
    itens = Atendimento.objects.filter(dataAtendimento__year=ano, dataAtendimento__month=mes, cliente_id = id).values('servico_id__pataz__qtdPontos', 'dataAtendimento', 'servico_id__descricao', 'servico_id', 'cliente__nome', 'pet_id__nome', 'pet_id__tipo').order_by('-dataAtendimento') 
    return JsonResponse({'itens' : list(itens), 'total': total})