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
def posiciona_frota(frota):
    
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]

    
    for tipo_navio in frota:
        for navio in frota[tipo_navio]:
            for posicao in navio:
                x, y = posicao
                tabuleiro[x][y] = 1

    return tabuleiro

