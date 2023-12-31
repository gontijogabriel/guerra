# Generated by Django 5.0 on 2023-12-29 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogador', '0002_alter_jogador_cor_alter_jogador_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True)),
                ('tropas', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='jogador',
            name='cartas',
            field=models.ManyToManyField(to='jogador.carta'),
        ),
        migrations.AddField(
            model_name='jogador',
            name='paises',
            field=models.ManyToManyField(to='jogador.pais'),
        ),
        migrations.CreateModel(
            name='PaisFronteiras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fronteiras', to='jogador.pais')),
                ('pais_fronteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fronteiras_fronteira', to='jogador.pais')),
            ],
        ),
    ]
