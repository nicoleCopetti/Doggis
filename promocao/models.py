from django.db import models
from servico.models import Servico
from produto.models import Produto

# Create your models here.

class Promocao(models.Model):
    dataInicial = models.DateTimeField(null=False)
    dataFinal = models.DateTimeField(null=False)
    percentualDesconto = models.IntegerField(null=False)

class PromocaoServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT)
    promocao = models.ForeignKey(Promocao, on_delete=models.RESTRICT)

class PromocaoProduto(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.RESTRICT)
    promocao = models.ForeignKey(Promocao, on_delete=models.RESTRICT)