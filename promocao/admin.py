from django.contrib import admin

from .models import Promocao, PromocaoProduto, PromocaoServico

admin.site.register(Promocao)
admin.site.register(PromocaoProduto)
admin.site.register(PromocaoServico)
