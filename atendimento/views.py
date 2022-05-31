from django.shortcuts import render
from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login
import json
from django.db import DatabaseError
from .models import Atendimento
from user.models import Atendente, Veterinario
from pet.models import Pet
from servico.models import Servico
import datetime

# @login_required(login_url='/user/login/')
def index(request):
    pets = Pet.objects.all()
    servicos = Servico.objects.all()
    return render(request,'atendimentos.html', { 'pets': pets, 'servicos': servicos }) 

def listarProfissional(request, pet = None):
    pets = Pet.objects.get(id = pet)
    veterinarios = Veterinario.objects.filter(tipoPetAtendimento__contains = pets.tipo).values('user_id', 'nome')
    atendetes = Atendente.objects.filter(tipoPetAtendimento__contains = pets.tipo).values('user_id', 'nome')
    return JsonResponse({'veterinarios' : list(veterinarios), 'atendentes': list(atendetes)})

def listarAtendimento(request, id = None):
    atendimento = Atendimento.objects.filter(id = id).values()
    return JsonResponse({'atendimento' : list(atendimento)})

def salvarAtendimento(request):
    try:
        dados = json.load(request)['dados']
        if dados['id'] == '':
            dados['id'] = None

        dia = int(dados['dataAtendimento'].split('T')[0].split('-')[2])
        mes = int(dados['dataAtendimento'].split('T')[0].split('-')[1])
        ano = int(dados['dataAtendimento'].split('T')[0].split('-')[0])
        hora = int(dados['dataAtendimento'].split('T')[1].split(':')[0])
        minuto = int(dados['dataAtendimento'].split('T')[1].split(':')[1])
        periodo = datetime.datetime(ano, mes, dia, hora, minuto)

        if Atendimento.objects.filter(profissional_id= dados['profissional'], dataAtendimento= periodo) and dados['id'] == None:
            return JsonResponse({}, status=401)
        else:
            pet = Pet.objects.get(id = dados['pet'])
            atendimento = Atendimento.objects.update_or_create(id = dados['id'], defaults={
                'cliente_id' : pet.cliente.id,
                'pet_id' : dados['pet'],
                'profissional_id' : dados['profissional'],
                'servico_id' : dados['servico'],
                'dataAtendimento' : dados['dataAtendimento'],
                'status' : dados['status'],
            })[0]
            atendimento.save()
            return JsonResponse({'retorno': 'ok'})
    except DatabaseError as a:
        return JsonResponse({'error': str(a)}, status=500)

def listarAtendimentos(request):
    atendimentos = Atendimento.objects.all().values('dataAtendimento', 'pet__nome', 'cliente__nome', 'servico__descricao', 'id')
    return JsonResponse({'atendimentos' : list(atendimentos)})

