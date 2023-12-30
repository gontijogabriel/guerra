from django.contrib import admin
from .models import Pais, PaisFronteiras, Carta, Jogador

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'tropas')

@admin.register(PaisFronteiras)
class PaisFronteirasAdmin(admin.ModelAdmin):
    list_display = ('id','pais', 'pais_fronteira')

@admin.register(Carta)
class CartaAdmin(admin.ModelAdmin):
    list_display = ('id','tipo',)

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'cor')
    filter_horizontal = ('paises', 'cartas')

