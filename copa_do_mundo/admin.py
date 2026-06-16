from django.contrib import admin
from .models import Jogador, Selecao, Juiz, Partida

# Register your models here.

admin.site.register(Jogador)
admin.site.register(Selecao)
admin.site.register(Juiz)
admin.site.register(Partida)
