def blackjack():
    print('')
    print('--- BlackJack ---')
#    print('')
    print('   1 - Jogar')
    print('   2 - Sair')
    print('')
    opt = input(' Opção: ')
    while opt not in ['1','2']:
        opt = input(' Opção inválida. Digite 1 ou 2: ')
    if opt == '2':
        return False
    else:
        ### cria jogadores
        jogadores = []
        n_jogadores = int(input('\nDigite o número de jogadores: '))
        while n_jogadores not in [1,2,3,4,5]:
            n_jogadores = int(input(' Jogo permite de 1 a 5 jogadores. Digite o número de jogadores: '))
        print('')
        for n in range(n_jogadores):
            nome = input(f'Digite o nome do jogador {n+1}: ')
            hand = []
            pontos = 0
            ativo = True
            jogador = [nome, hand, pontos, ativo]
            jogadores.append(jogador)
    
    ### cria o deck de cartas para o jogo
    print('')
    n_baralhos = int(input('Digite o número de baralhos no jogo: '))
    while n_baralhos not in [1,2,3,4]:
            n_baralhos = int(input(' Você pode jogar com até 4 baralhos. Digite o número de baralhos no jogo: '))
    deck = baralho(n_baralhos)
    
    ### faz a abertura do jogo chamando a primeira carta de cada jogador
    print('')
    print('Primeira rodada')
    print('---------------------------------------')
    for jogador in jogadores:
        carta = call(deck)
        jogador[1].append(carta)
        jogador[2] += pontos_carta(carta)
    placar(jogadores)
    
    ### chama o próximo jogador ativo enquanto houver jogadores ativos
    ativos = True
    while ativos:
        ativos = False
        for jogador in jogadores:
            if jogador[3] == True:
                play(jogador, jogadores, deck)
                ativos = True
  
    ### verifica o vencedor
    vencedor = verifica_pontuacao(jogadores)
    if len(vencedor) == 1:
        print(f'\n --- {vencedor[0][0]} venceu o jogo! ---\n\n')
    else:
        vencedores = ''
        for jogador in vencedor:
            if jogador == vencedor[0]:
                vencedores += jogador[0]
            elif jogador == vencedor[-1]:
                vencedores += ' e ' + jogador[0]
            else:
                vencedores += ', ' + jogador[0]
        print(f'\n --- {vencedores} empataram o jogo! ---\n\n')
    return True

        
def baralho(n_baralhos):
    alfa = ['A','2','3','4','5','6','7','8','9','10','J','D','K']
    naipes = ['♥','♦','♣','♠']
    deck = []
    for n in range(n_baralhos):  ## pensar em usar compreensão de listas
        for i in naipes:
            for j in alfa:
                deck.append(j+i)
    print('')
    print(f'Criado um deck com {n_baralhos} baralho(s) e {len(deck)} cartas.')
    return deck


def play(jogador, jogadores, deck):
    opt = input(f'\n{jogador[0]}, quer outra carta [c] ou parar [p]? ')
    while opt not in ['c','p']:
        opt = input(f'{jogador[0]}, pressione [c] para continuar ou [p] para parar: ')
    if opt == 'p':
        print('---------------------------------------')
        placar(jogadores)
        jogador[3] = False
        print(f'{jogador[0]} parou.')
    else:
        carta = call(deck)
        jogador[1].append(carta)
        jogador[2] += pontos_carta(carta)
        print('---------------------------------------')
        placar(jogadores)
        if jogador[2] > 21:
            jogador[3] = False
            print(f'{jogador[0]} estourou.')


def call(deck):
    import random
    return deck.pop(random.randint(0,len(deck)-1))

       
def pontos_carta(carta):
    if carta[0] in ['2','3','4','5','6','7','8','9']:
        return int(carta[0])
    elif carta [0] == 'A':
        return 1
    else:
        return 10    


def placar(jogadores):
    for jogador in jogadores:
        print(f'{jogador[0]}: {jogador[1]} - {jogador[2]} pontos')


def verifica_pontuacao(jogadores):
    maior = 0
    vencedores = []
    for jogador in jogadores:
        if jogador[2] < 22 and jogador[2] > maior:
            maior = jogador[2]
    for jogador in jogadores:
        if jogador[2] == maior:
            vencedores.append(jogador)
    return vencedores


while blackjack():
    continue