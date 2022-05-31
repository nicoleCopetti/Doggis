from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=120, null=False)
    cpf = models.CharField(max_length=14, null=False)
    identidade = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, related_name='Cliente', on_delete=models.RESTRICT)

class Veterinario(models.Model):
    nome = models.CharField(max_length=120, null=False)
    cpf = models.CharField(max_length=14, null=False)
    identidade = models.CharField(max_length=20, null=True)
    CRMV = models.CharField(max_length=10, null=False)
    user = models.OneToOneField(User, related_name='Veterinario', on_delete=models.RESTRICT)
    tipoPetAtendimento = models.CharField(max_length=120, null=True)

class Atendente(models.Model):
    nome = models.CharField(max_length=120, null=False)
    cpf = models.CharField(max_length=14, null=False)
    identidade = models.CharField(max_length=20, null=True)
    user = models.OneToOneField(User, related_name='Atendente', on_delete=models.RESTRICT)
    tipoPetAtendimento = models.CharField(max_length=120, null=True)