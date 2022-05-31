from django.db import models
from produto.models import Produto
from datetime import datetime

# Create your models here.

class Servico(models.Model):
    descricao = models.CharField(max_length=80, null=False)
    tempoEstimado = models.TimeField(null=False)
    preco = models.DecimalField(decimal_places = 2, max_digits = 8, null=True)

    def qtdPataz(self):
        pataz =Pataz.objects.get(servico_id = self.id)
        return pataz.qtdPontos

class ProdutoServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT)
    produto = models.ManyToManyField(Produto)

class Pataz(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT)
    qtdPontos = models.IntegerField(null=False)
    qtdMinimaBrinde = models.IntegerField(null=False)

class HistoricoPrecoServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT)
    preco = models.DecimalField(decimal_places = 2, max_digits = 8, null=True)
    dataAlteracao = models.DateTimeField(default=datetime.now, blank=True)
    usuarioAteracao = models.CharField(max_length=80, null=False)

