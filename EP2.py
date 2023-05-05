import random

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'horizontal':
            posicoes.append([linha, coluna + i])
        else:
            posicoes.append([linha + i, coluna])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)
    
    if nome_navio in frota:
        frota[nome_navio].append(posicoes_navio)
    else:
        frota[nome_navio] = [posicoes_navio]

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

def afundados(frota, tabuleiro):
    navios_afundados = 0

    for tipo_navio, posicoes_navios in frota.items():
        for navio in posicoes_navios:
            afundado = True
            for posicao in navio:
                x, y = posicao
                if tabuleiro[x][y] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1

    return navios_afundados

def posicao_valida(frota, linha, coluna, orientacao, tamanho):

    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)


    for posicao in posicoes:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False


    for tipo_navio, navios in frota.items():
        for navio in navios:
            for posicao_navio in navio:
                if posicao_navio in posicoes:
                    return False


    return True

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
}

navios = [
    ("porta-aviões", 4),
    ("navio-tanque", 3),
    ("navio-tanque", 3),
    ("contratorpedeiro", 2),
    ("contratorpedeiro", 2),
    ("contratorpedeiro", 2),
    ("submarino", 1),
    ("submarino", 1),
    ("submarino", 1),
    ("submarino", 1),
]

for navio, tamanho in navios:
    while True:
        print(f"Insira as informações referentes ao navio {navio} que possui tamanho {tamanho}")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if tamanho > 1:
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
            orientacao = 'vertical' if orientacao == 1 else 'horizontal'
        else:
            orientacao = None

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
            preenche_frota(frota, navio, linha, coluna, orientacao, tamanho)  
            break
        else:
            print("Esta posição não está válida!")

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

# Dicionário da frota do oponente
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for _ in range(10)]

    for tipo_navio, navios in frota.items():
        for navio in navios:
            for posicao in navio:
                x, y = posicao
                tabuleiro[x][y] = 1

    return tabuleiro


tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)


jogando = True


posicoes_informadas = []
posicoes_oponente_informadas = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    
    
    while True:
        linha = int(input("Informe a linha em que deseja atacar (0-9): "))
        if linha >= 0 and linha <= 9:
            break
        print("Linha inválida!")

    
    while True:
        coluna = int(input("Informe a coluna em que deseja atacar (0-9): "))
        if coluna >= 0 and coluna <= 9:
            break
        print("Coluna inválida!")
    
    
    if (linha, coluna) in posicoes_informadas:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        continue

    
    posicoes_informadas.append((linha, coluna))

    
    faz_jogada(tabuleiro_oponente, linha, coluna)

    
    if afundados(frota_oponente, tabuleiro_oponente) == len(navios):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
        
    if afundados(frota_oponente, tabuleiro_oponente) != len(navios):
        
        while True:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

            if (linha_oponente, coluna_oponente) not in posicoes_oponente_informadas:
                break

        posicoes_oponente_informadas.append((linha_oponente, coluna_oponente))
        print(f"Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}")

        
        faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        
        if afundados(frota, tabuleiro_jogador) == len(navios):
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False
        






