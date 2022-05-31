from django.db import models
from user.models import Cliente

class Pet(models.Model):
    nome = models.CharField(max_length=80, null=False)
    raca = models.CharField(max_length=80, null=False)
    tipo = models.CharField(max_length=80, choices=(('Cão', 'Cão'), ('Gato', 'Gato'), ('Roedor', 'Roedor'), ('Peixe', 'Peixe'), ('Réptil', 'Réptil'), ('Ave', 'Ave')), default='Cão')
    porte = models.CharField(max_length=10, choices=(('Pequeno', 'Pequeno'), ('Média', 'Média'), ('Grande', 'Grande')), default='Média')
    alergia = models.CharField(max_length=200, null=True)
    descHabitosGostos = models.CharField(max_length=200, null=True)
    autorizacaoUsoImagem = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
