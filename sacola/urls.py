from django.urls import path
from . import views

app_name = 'sacola'

urlpatterns = [
    path('', views.index, name='index'),
    path('listarServico/<int:id>', views.listarServico, name='listarServico'),
    path('listarProduto/<int:id>', views.listarProduto, name='listarProduto'),
    # path('salvarProduto', views.salvarProduto, name='salvarProduto'),
    # path('listarProdutos', views.listarProdutos, name='listarProdutos'),
    # path('listarProduto/<int:id>', views.listarProduto, name='listarProduto'),
    # path('excluirProduto/<int:id>', views.excluirProduto, name='excluirProduto'),
]