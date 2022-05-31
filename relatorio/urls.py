from django.urls import path
from . import views

app_name = 'relatorio'

urlpatterns = [
    path('', views.index, name='index'),
    path('relServicoProfissional/<int:id>/<int:ano>/<int:mes>', views.relServicoProfissional, name='relServicoProfissional'),
    path('relServicoCliente/<int:id>/<int:ano>/<int:mes>', views.relServicoCliente, name='relServicoCliente')
]