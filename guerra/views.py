from django.shortcuts import render, get_object_or_404, redirect
from jogador.models import Jogador, Carta, Pais
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
    paises = ['BRA','URU','ARG','BOL','PER','CHI','PAR','EQU','COL','VEN','SUR','GUI']


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
    sortear_paises_para_jogadores()
    return redirect('startGame', jogador_atual_id=1)


def startGame(request, jogador_atual_id):
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
    # Pega os paises de posse do jogador e multiplica por 2x
    paises_do_jogador = Jogador.objects.get(nome=jogador_vez_nome)
    lista_paises = list(map(lambda item: item['nome'], paises_do_jogador.paises.values('nome')))
    tropas_para_distribuir = len(lista_paises) * 2

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
        'tropas_para_distribuir': tropas_para_distribuir,
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



# Fronteiras

# 34	GUI	VEN
# 33	GUI	SUR
# 32	SUR	GUI
# 31	SUR	VEN
# 30	SUR	BRA
# 29	VEN	COL
# 28	VEN	SUR
# 27	VEN	GUI
# 26	COL	VEN
# 25	COL	VEN
# 24	COL	PAR
# 23	EQU	COL
# 22	EQU	PAR
# 21	PAR	EQU
# 20	PAR	COL
# 19	PAR	CHI
# 18	CHI	PAR
# 17	CHI	PER
# 16	CHI	BOL
# 15	PER	CHI
# 14	PER	BOL
# 13	PER	BRA
# 12	BOL	CHI
# 11	BOL	PER
# 10	BOL	ARG
# 9	    ARG	BOL
# 8	    ARG	BRA
# 7	    ARG	URU
# 6	    URU	ARG
# 5	    URU	BRA
# 4	    BRA	SUR
# 3	    BRA	PER
# 2	    BRA	ARG
# 1	    BRA	URU


# Cartas

# 4	🤡
# 3	🟩
# 2	🟡
# 1	🔺