from django.urls import path
from . import views

app_name = 'atendimento'

urlpatterns = [
    path('', views.index, name='index'),
    path('listarProfissional/<int:pet>', views.listarProfissional, name='listarProfissional'),
    path('salvarAtendimento', views.salvarAtendimento, name='salvarAtendimento'),
    path('listarAtendimentos', views.listarAtendimentos, name='listarAtendimentos'),
    path('listarAtendimento/<int:id>', views.listarAtendimento, name='listarAtendimento'),
]