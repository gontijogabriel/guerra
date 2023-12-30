from django.urls import path
from guerra.views import ( index, excluirJogador, startGame, proximoJogador, 
                          default, adicionarTropa 
)

from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('', index, name='home'),
    path('excluir-jogador/<int:jogador_id>/', excluirJogador, name='excluir_jogador'),
    path('default/', default, name='default'),
    path('game/<int:jogador_atual_id>/', startGame, name='startGame'),
    path('game/', proximoJogador, name='proximoJogador'),

    path('game/adicionar-tropa/', adicionarTropa, name='adicionarTropa')
]