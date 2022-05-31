from django.shortcuts import render
from .models import Produto
from servico.models import ProdutoServico
from django.http import JsonResponse
from django.db import DatabaseError
import json

def index(request):
    produtos = Produto.objects.all()
    return render(request,'produtos.html', { 'produtos': produtos }) 

def listarProdutos(request):
    produtos = Produto.objects.all().values()
    return JsonResponse({'produtos' : list(produtos)})

def listarProduto(request, id = None):
    produto = Produto.objects.filter(id=id).values()
    return JsonResponse({'produto' : list(produto)})

def salvarProduto(request):
    try:
        dados = json.load(request)['dados']
        if dados['id'] == '':
            dados['id'] = None

        produto = Produto.objects.update_or_create(id = dados['id'], defaults={
            'nome' : dados['descricao'],
            'fabricante' : dados['fabricante'],
            'especificacao' : dados['especificacao'],
            'precoVenda' : dados['preco'],
            'quantidade' : dados['qtd'],
        })[0]
        produto.save()
        return JsonResponse({'retorno': 'ok'})
    except DatabaseError as a:
        return JsonResponse({'error': str(a)}, status=500)

def excluirProduto(request, id = None):
    try:
        if ProdutoServico.objects.filter(produto = id):
            return JsonResponse({}, status=401)
        else:
            Produto.objects.filter(id = id).delete()
        return JsonResponse({'retorno': 'ok'})
    except DatabaseError as a:
        return JsonResponse({'error': str(a)}, status=500)