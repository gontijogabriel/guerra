from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    tropas_distribuir = models.IntegerField(default=0)
    paises = models.ManyToManyField('pais', related_name='jogadores')
    cartas = models.ManyToManyField('carta', related_name='jogadores')