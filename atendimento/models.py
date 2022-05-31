from django.db import models
from user.models import User, Cliente
from pet.models import Pet
from servico.models import Servico

class Atendimento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    pet = models.ForeignKey(Pet, on_delete=models.RESTRICT)
    profissional = models.ForeignKey(User, on_delete=models.RESTRICT)
    servico = models.ForeignKey(Servico, on_delete=models.RESTRICT)
    dataAtendimento = models.DateTimeField(null=False)
    status = models.CharField(max_length=10, choices=(('1', 'Aguardando Atendimento'), ('2', 'Cancelado'), ('3', 'Concluído')), default='1')

   