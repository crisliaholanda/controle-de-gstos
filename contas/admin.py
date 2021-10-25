from django.contrib import admin
from .models import Categoria, Transacao

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin): 
    list_display = ('nome', 'dt_criacao',)

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = (
        'data','descriacao',
        'valor', 'categoria',
        'observacoes',
        )