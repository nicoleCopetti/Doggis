from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=80, null=False)
    fabricante = models.CharField(max_length=120, null=True)
    especificacao = models.CharField(max_length=400, null=True)
    precoVenda = models.DecimalField(decimal_places = 2, max_digits = 8, null=True)
    quantidade = models.IntegerField(null=True)
