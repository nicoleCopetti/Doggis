from django.shortcuts import render
from django.http import JsonResponse
from django.db import DatabaseError
import json
from atendimento.models import Atendimento
from user.models import Atendente, Veterinario
from pet.models import Pet
from servico.models import Servico
from produto.models import Produto

def index(request):
    pets = Pet.objects.all()
    servicos = Servico.objects.all()
    produtos = Produto.objects.all()
    return render(request,'pagamento.html', { 'pets': pets, 'servicos': servicos, 'produtos': produtos }) 

def listarServico(request, id = None):
    servico = Servico.objects.filter(id = id).values()
    return JsonResponse({'servicos' : list(servico)})

def listarProduto(request, id = None):
    produto = Produto.objects.filter(id = id).values()
    return JsonResponse({'produtos' : list(produto)})