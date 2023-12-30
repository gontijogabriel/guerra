from django.db import models

class Pais(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    tropas = models.IntegerField(null=False, blank=False, default=1)
    jogador = models.ForeignKey('Jogador', on_delete=models.SET_NULL, null=True, blank=True, related_name='paises_jogador')

    def __str__(self):
        return f'{self.nome}'

class PaisFronteiras(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='fronteiras')
    pais_fronteira = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='fronteiras_fronteira')

    def __str__(self):
        return f'{self.pais} - {self.pais_fronteira}'

class Carta(models.Model):
    tipo = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.tipo

class Jogador(models.Model):
    nome = models.CharField(max_length=255, unique=True, null=False, blank=False)
    cor = models.CharField(max_length=255, unique=True, null=False, blank=False)
    paises = models.ManyToManyField(Pais, related_name='jogadores')
    cartas = models.ManyToManyField(Carta)
    distribuindo_tropas = models.BooleanField(null=True, blank=True, default=False)
    tropas_distribuir = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome
