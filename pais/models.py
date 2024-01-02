from django.db import models
from jogador.models import Jogador

class Pais(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tropas = models.IntegerField(default=1)
    paises_fronteira = models.ManyToManyField('pais', related_name='fronteiras')
