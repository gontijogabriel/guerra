from django.shortcuts import render, get_object_or_404, redirect
from jogador.models import Jogador, Carta, Pais, PaisFronteiras
import random


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cor = request.POST.get('cor')

        if not Jogador.objects.filter(nome=nome).exists() and not Jogador.objects.filter(cor=cor).exists():
            novo_jogador = Jogador(nome=nome, cor=cor)
            novo_jogador.save()
            jogadores = Jogador.objects.all()
            return render(request, 'index.html', {'jogadores': jogadores})
        else:
            jogadores = Jogador.objects.all()
            msg = 'dados incorretos'
            return render(request, 'index.html', {'jogadores': jogadores, 'msg': msg})
        
    jogadores = Jogador.objects.all()
    return render(request, 'index.html', {'jogadores': jogadores})


def excluirJogador(request, jogador_id):
    jogador = get_object_or_404(Jogador, id=jogador_id)
    jogador.delete()
    return redirect('home')


def limpa_dados_do_db():
    print()


def adiciona_paises_no_db():
    # limpa todas as linhas existentes na tabela Pais
    Pais.objects.all().delete()

    paises = [
        {'nome': 'BRA', 'tropas': 1},
        {'nome': 'URU', 'tropas': 1},
        {'nome': 'ARG', 'tropas': 1},
        {'nome': 'BOL', 'tropas': 1},
        {'nome': 'PER', 'tropas': 1},
        {'nome': 'CHI', 'tropas': 1},
        {'nome': 'PAR', 'tropas': 1},
        {'nome': 'EQU', 'tropas': 1},
        {'nome': 'COL', 'tropas': 1},
        {'nome': 'VEN', 'tropas': 1},
        {'nome': 'SUR', 'tropas': 1},
        {'nome': 'GUI', 'tropas': 1},
    ]

    for pais_info in paises:
        Pais.objects.create(nome=pais_info['nome'], tropas=pais_info['tropas'])

    print('Tabela de Paises Atualizadas')


    # Limpa todos os dados existentes na tabela Fronteiras
    PaisFronteiras.objects.all().delete()

    dados_fronteiras = [
        {'id': 34, 'pais': 'GUI', 'pais_fronteira': 'VEN'},
        {'id': 33, 'pais': 'GUI', 'pais_fronteira': 'SUR'},
        {'id': 32, 'pais': 'SUR', 'pais_fronteira': 'GUI'},
        {'id': 31, 'pais': 'SUR', 'pais_fronteira': 'VEN'},
        {'id': 30, 'pais': 'SUR', 'pais_fronteira': 'BRA'},
        {'id': 29, 'pais': 'VEN', 'pais_fronteira': 'COL'},
        {'id': 28, 'pais': 'VEN', 'pais_fronteira': 'SUR'},
        {'id': 27, 'pais': 'VEN', 'pais_fronteira': 'GUI'},
        {'id': 26, 'pais': 'COL', 'pais_fronteira': 'VEN'},
        {'id': 25, 'pais': 'COL', 'pais_fronteira': 'VEN'},
        {'id': 24, 'pais': 'COL', 'pais_fronteira': 'PAR'},
        {'id': 23, 'pais': 'EQU', 'pais_fronteira': 'COL'},
        {'id': 22, 'pais': 'EQU', 'pais_fronteira': 'PAR'},
        {'id': 21, 'pais': 'PAR', 'pais_fronteira': 'EQU'},
        {'id': 20, 'pais': 'PAR', 'pais_fronteira': 'COL'},
        {'id': 19, 'pais': 'PAR', 'pais_fronteira': 'CHI'},
        {'id': 18, 'pais': 'CHI', 'pais_fronteira': 'PAR'},
        {'id': 17, 'pais': 'CHI', 'pais_fronteira': 'PER'},
        {'id': 16, 'pais': 'CHI', 'pais_fronteira': 'BOL'},
        {'id': 15, 'pais': 'PER', 'pais_fronteira': 'CHI'},
        {'id': 14, 'pais': 'PER', 'pais_fronteira': 'BOL'},
        {'id': 13, 'pais': 'PER', 'pais_fronteira': 'BRA'},
        {'id': 12, 'pais': 'BOL', 'pais_fronteira': 'CHI'},
        {'id': 11, 'pais': 'BOL', 'pais_fronteira': 'PER'},
        {'id': 10, 'pais': 'BOL', 'pais_fronteira': 'ARG'},
        {'id': 9, 'pais': 'ARG', 'pais_fronteira': 'BOL'},
        {'id': 8, 'pais': 'ARG', 'pais_fronteira': 'BRA'},
        {'id': 7, 'pais': 'ARG', 'pais_fronteira': 'URU'},
        {'id': 6, 'pais': 'URU', 'pais_fronteira': 'ARG'},
        {'id': 5, 'pais': 'URU', 'pais_fronteira': 'BRA'},
        {'id': 4, 'pais': 'BRA', 'pais_fronteira': 'SUR'},
        {'id': 3, 'pais': 'BRA', 'pais_fronteira': 'PER'},
        {'id': 2, 'pais': 'BRA', 'pais_fronteira': 'ARG'},
        {'id': 1, 'pais': 'BRA', 'pais_fronteira': 'URU'},
    ]

    for fronteira_info in dados_fronteiras:
        pais_origem = Pais.objects.get(nome=fronteira_info['pais'])
        pais_fronteira = Pais.objects.get(nome=fronteira_info['pais_fronteira'])
        
        PaisFronteiras.objects.create(
            id=fronteira_info['id'],
            pais=pais_origem,
            pais_fronteira=pais_fronteira
        )

    print('Tabela de Fronteiras Atualizadas')

    Carta.objects.all().delete()

    dados_cartas = [
        {'valor': 1, 'icone': '🤡'},
        {'valor': 2, 'icone': '🟩'},
        {'valor': 3, 'icone': '🟡'},
        {'valor': 4, 'icone': '🔺'},
    ]

    for carta_info in dados_cartas:
        Carta.objects.create(
            tipo=carta_info['icone'],
        )

    print('Tabela de Cartas Atualizadas')


def sortear_paises_para_jogadores():
    paises = Pais.objects.all()
    jogadores = Jogador.objects.all()

    paises_embaralhados = random.sample(list(paises), len(paises))

    paises_por_jogador = len(paises) // len(jogadores)

    for i, jogador in enumerate(jogadores):
        paises_do_jogador = paises_embaralhados[i * paises_por_jogador: (i + 1) * paises_por_jogador]
        jogador.paises.set(paises_do_jogador)

        for pais in paises_do_jogador:
            pais.jogador = jogador
            pais.save()

    print('sorteou paises para jogadores')


def default(request):
    adiciona_paises_no_db()
    sortear_paises_para_jogadores()

    return redirect('startGame', jogador_atual_id=1)



# Deve ser chamada sempre quando for DISTRIBUIR TROPAS do jogador
def distribuicao_de_tropas(nome_jogador):
    # Retorna quantas tropas cada jogador vai ter para distribuir
    # Pega os paises de posse do jogador e multiplica por 2x
    jogador = Jogador.objects.get(nome=nome_jogador)
    lista_paises = list(map(lambda item: item['nome'], jogador.paises.values('nome')))

    jogador.tropas_distribuir = len(lista_paises) * 2
    jogador.save()

    print(f'Tropas Distribuidas para jogador: {jogador} / Tropas: {len(lista_paises) * 2}')



def startGame(request, jogador_atual_id):

    ################################# Atualiza dados de Paises e Jogadores #################################

    paises = Pais.objects.all()
    jogadores = Jogador.objects.all()

    dados_jogadores = {}
    dados_paises = {}

    for jogador in jogadores:
        dados_jogador = {
            'nome': jogador.nome,
            'cor': jogador.cor,
            'paises': [pais.nome for pais in jogador.paises.all()],
            'cartas': [carta.tipo for carta in jogador.cartas.all()],
        }
        dados_jogadores[jogador.id] = dados_jogador

    for pais in paises:
        dados_pais = {
            'nome': pais.nome,
            'tropas': pais.tropas,
            'jogador': {
                'nome': pais.jogador.nome if pais.jogador else None,
                'cor': pais.jogador.cor if pais.jogador and pais.jogador.cor else 'gray',
            },
        }
        dados_paises[pais.nome] = dados_pais

    ##############################################################################################

    jogadores_list = list(jogadores)

    ids_jogadores = [(jogador.id, jogador.nome) for jogador in jogadores_list]

    if jogador_atual_id is None:
        jogador_atual_id = ids_jogadores[0][0]
    else:
        jogador_atual_id = int(jogador_atual_id)
        index_jogador_atual = next((i for i, (id, nome) in enumerate(ids_jogadores) if id == jogador_atual_id), None)

        if index_jogador_atual is not None:
            proximo_index = (index_jogador_atual + 1) % len(jogadores_list)
            jogador_atual_id = ids_jogadores[proximo_index][0]

    jogador_vez_nome = jogadores_list[jogador_atual_id - 1]

    # Tropas para distribuir
    distribuicao_de_tropas(jogador_vez_nome)

    # Imprima o jogador e os países
    #print(f'Jogador: {paises_do_jogador}, Países: {lista_paises}, Tropas: {tropas_para_distribuir}, a: {len(lista_paises)}')
    # print(f'paises: {dados_paises}')
    # print(f'jogadores: {dados_jogadores}')
    # for jogador_id, jogador_data in dados_jogadores.items():
    #     print(f'Nome do jogador com ID {jogador_id}: {jogador_data["nome"]}')
    # contexto = {
    #     'distribuir': True,
    #     'atacar': False,
    #     'remanejar': False,
    #     'paises': dados_paises,
    #     'jogador_vez_nome': jogador_vez_nome,
    #     'jogadores': dados_jogadores,
    #     'jogador_atual_id': jogador_atual_id,
    #     'ids_jogadores': ids_jogadores,
    #     'tropas_para_distribuir': tropas_para_distribuir,
    #     'lista_paises_jogador_atual': lista_paises,
    # }

    return render(request, 'game.html', {
        'distribuir': True,
        'atacar': False,
        'remanejar': False,
        'paises': dados_paises,
        'jogador_vez_nome': jogador_vez_nome,
        'jogadores': dados_jogadores,
        'jogador_atual_id': jogador_atual_id,
        'ids_jogadores': ids_jogadores,
        'tropas_para_distribuir': Jogador.objects.get(nome=jogador_vez_nome).tropas_distribuir,
        'lista_paises_jogador_atual': lista_paises,
    })


def adicionarTropa(request):
    # Pegar a quantidade de tropas que ele tem pra distribuir
    # Verificar se a posse do pais é do jogador
    # Adicionar a tropa no pais
    # Se a quantidade de tropas pra distribuir é igual a 1, o return deve passar para ATAQUE

    if request.method == 'POST':
        pais_distribuir = request.POST.get('inputPaisDistribuir')
        jogador_atual = request.POST.get('jogador_atual_id')
        lista_paises_jogador_atual = request.POST.get('lista_paises_jogador_atual')
        tropas_para_distribuir = request.POST.get('tropas_para_distribuir')

        if pais_distribuir != 'default_value' and pais_distribuir in lista_paises_jogador_atual:
            pais = Pais.objects.get(nome=pais_distribuir)
            pais.tropas = pais.tropas + 1
            pais.save()

            return redirect('startGame', int(jogador_atual))
        else:
            print('pais nao pertence ao jogador!')
            return redirect('startGame', int(jogador_atual))




def proximoJogador(request):
    jogadores_list = list(Jogador.objects.all())

    if request.method == 'POST':
        jogador_atual_id = request.POST.get('jogador_atual_id')
        if int(jogador_atual_id) == len(jogadores_list):
            jog = 1
        else:
            jog = int(jogador_atual_id) + 1
    return redirect('startGame', jogador_atual_id=jog)

