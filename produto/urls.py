from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.index, name='index'),
    path('salvarProduto', views.salvarProduto, name='salvarProduto'),
    path('listarProdutos', views.listarProdutos, name='listarProdutos'),
    path('listarProduto/<int:id>', views.listarProduto, name='listarProduto'),
    path('excluirProduto/<int:id>', views.excluirProduto, name='excluirProduto'),
]