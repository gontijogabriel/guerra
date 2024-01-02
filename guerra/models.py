from django.db import models
from jogador.models import Jogador

class Jogo(models.Model):

    jogador_atual = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    numero_trocas = models.IntegerField(default=0)
    rodada = models.IntegerField(default=1)
    fase = models.CharField(max_length=50, default='d')

    # Fases do jogo
    # "d" Distribuir Tropas
    # "a" Atacar
    # "r" Remanejar

class Carta(models.Model):

    carta = models.CharField(max_length=100)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)

    # 🤡
    # 🟩
    # 🟡
    # 🔺