
ESQUERDA = 'esquerda'
ACIMA = 'acima'
DIREITA = 'direita'
ABAIXO = 'abaixo'

def linha_to_matriz(str_puzzle):
    """Conversão do String para Matriz"""
    linha1 = []
    linha2 = []
    linha3 = []
    mtz_puzzle = []
    for i in range(0, len(str_puzzle)):
        if i < 3:
            linha1.append(str_puzzle[i])
        elif (i >= 3) and (i < 6):
            linha2.append(str_puzzle[i])
        else:
            linha3.append(str_puzzle[i])

    mtz_puzzle.append(linha1)
    mtz_puzzle.append(linha2)
    mtz_puzzle.append(linha3)
    return mtz_puzzle


def matriz_to_linha(mtz_puzzle):
    """Conversão da Matriz para String"""
    puzzle_string = ''
    for i in range(0, len(mtz_puzzle)):
        for j in range(0, len(mtz_puzzle[i])):
            puzzle_string += mtz_puzzle[i][j]

    return puzzle_string


def imprime_matriz(matriz):
    """Imprime o Estado Atual da Matriz"""
    print('---------------')
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print('---------------')


def sucessor(estado):
    """recebe string estado ex: '2_3541687';
       retorna uma lista de tuplas (ação, estado_atingido)"""
    matriz = linha_to_matriz(estado)
    lin = -1
    col = -1
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == '_':
                lin = i
                col = j
                break

    return get_acoes(lin, col, matriz)

def get_acoes(lin, col, matriz):
    lista_acao_estadoatingido = []
    str_puzzle = ''

    if lin == 0:
        if col == 0:  # direita; abaixo; = ok
            lista_acao_estadoatingido.append((DIREITA, get_string_acao(lin, col, matriz, DIREITA)))
            lista_acao_estadoatingido.append((ABAIXO, get_string_acao(lin, col, matriz, ABAIXO)))

        elif col == 1:  # esquerda; direita; abaixo; = ok
            lista_acao_estadoatingido.append((ESQUERDA, get_string_acao(lin, col, matriz, ESQUERDA)))
            lista_acao_estadoatingido.append((DIREITA, get_string_acao(lin, col, matriz, DIREITA)))
            lista_acao_estadoatingido.append((ABAIXO, get_string_acao(lin, col, matriz, ABAIXO)))

        elif col == 2:  # esquerda; abaixo;
            lista_acao_estadoatingido.append((ESQUERDA, get_string_acao(lin, col, matriz, ESQUERDA)))
            lista_acao_estadoatingido.append((ABAIXO, get_string_acao(lin, col, matriz, ABAIXO)))

        elif lin == 1:
            if col == 0:  # acima; direita; abaixo;
                lista_acao_estadoatingido.append((ACIMA, get_string_acao(lin, col, matriz, ACIMA)))
                lista_acao_estadoatingido.append((DIREITA, get_string_acao(lin, col, matriz, DIREITA)))
                lista_acao_estadoatingido.append((ABAIXO, get_string_acao(lin, col, matriz, ABAIXO)))

            elif col == 1:  # esquerda; acima; direita; abaixo;
                lista_acao_estadoatingido.append((ESQUERDA, get_string_acao(lin, col, matriz, ESQUERDA)))
                lista_acao_estadoatingido.append((ACIMA, get_string_acao(lin, col, matriz, ACIMA)))
                lista_acao_estadoatingido.append((DIREITA, get_string_acao(lin, col, matriz, DIREITA)))
                lista_acao_estadoatingido.append((ABAIXO, get_string_acao(lin, col, matriz, ABAIXO)))

            elif col == 2:  # esquerda; acima; abaixo;
                lista_acao_estadoatingido.append((ESQUERDA, get_string_acao(lin, col, matriz, ESQUERDA)))
                lista_acao_estadoatingido.append((ACIMA, get_string_acao(lin, col, matriz, ACIMA)))
                lista_acao_estadoatingido.append((ABAIXO, get_string_acao(lin, col, matriz, ABAIXO)))

        elif lin == 2:
            if col == 0:  # acima; direita;
                lista_acao_estadoatingido.append((ACIMA, get_string_acao(lin, col, matriz, ACIMA)))
                lista_acao_estadoatingido.append((DIREITA, get_string_acao(lin, col, matriz, DIREITA)))

            elif col == 1:  # esquerda; acima; direita
                lista_acao_estadoatingido.append((ESQUERDA, get_string_acao(lin, col, matriz, ESQUERDA)))
                lista_acao_estadoatingido.append((ACIMA, get_string_acao(lin, col, matriz, ACIMA)))
                lista_acao_estadoatingido.append((DIREITA, get_string_acao(lin, col, matriz, DIREITA)))

            elif col == 2:  # esquerda; acima
                lista_acao_estadoatingido.append((ESQUERDA, get_string_acao(lin, col, matriz, ESQUERDA)))
                lista_acao_estadoatingido.append((ACIMA, get_string_acao(lin, col, matriz, ACIMA)))

    return lista_acao_estadoatingido


# @doing now

def get_string_acao(lin, col, matriz, acao):
    mtz = [matriz[0].copy(), matriz[1].copy(), matriz[2].copy()]
    aux = mtz[lin][col]

    if acao == ESQUERDA:
        print("ESQUERDA")
        imprime_matriz(mtz)
        mtz[lin][col] = mtz[lin][col - 1]
        mtz[lin][col - 1] = aux
        imprime_matriz(mtz)

    elif acao == DIREITA:
        print("DIREITA")
        imprime_matriz(mtz)
        mtz[lin][col] = mtz[lin][col + 1]
        mtz[lin][col + 1] = aux
        imprime_matriz(mtz)

    elif acao == ACIMA:
        print("ACIMA")
        imprime_matriz(mtz)
        mtz[lin][col] = mtz[lin - 1][col]
        mtz[lin - 1][col] = aux
        imprime_matriz(mtz)

    elif acao == ABAIXO:
        print("ABAIXO")
        imprime_matriz(mtz)
        mtz[lin][col] = mtz[lin + 1][col]
        mtz[lin + 1][col] = aux
        imprime_matriz(mtz)

    return matriz_to_linha(mtz)


def get_indices_vazio():
    indices_vazio = []
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if matriz[i][j] == '_':
                indices_vazio.append(i)
                indices_vazio.append(j)
                return indices_vazio


'''
def expande(nodo):
    sucessor(nodo.estado)
    print(nodo.estado)
'''
'''========================================================================================='''


class Nodo:
    '''construtor default python'''

    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        ##self.next = None ##? right_sun, left_sun,... --> NOP

    def __repr__(self):
        """override toString default python"""
        return '%s  %s %s %s' % (self.estado, self.pai, self.acao, self.custo)
