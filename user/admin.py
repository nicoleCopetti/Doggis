from django.contrib import admin

from .models import Cliente, Veterinario, Atendente

admin.site.register(Cliente)
admin.site.register(Veterinario)
admin.site.register(Atendente)

