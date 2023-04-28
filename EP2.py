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


