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
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])


def sucessor(estado):
    """recebe string estado '_23541687';
       retorna uma lista de tuplas (ação, estado_atingido)"""
    matriz = linha_to_matriz(estado)
    lista_de_tuplas = get_transicoes(matriz)

    return lista_de_tuplas


def get_transicoes(matriz):
    """retorna as transicoes possiveis"""
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
        if col == 0:  # direita; abaixo;
            str_puzzle = get_string_acao(lin, col, matriz, DIREITA)
            tupla1 = (DIREITA, str_puzzle)
            str_puzzle = get_string_acao(lin, col, matriz, ABAIXO)
            tupla2 = (ABAIXO, str_puzzle)
            lista_acao_estadoatingido.append(tupla1)
            lista_acao_estadoatingido.append(tupla2)
        elif col == 1:  # esquerda; direita; abaixo
            tupla1 = (DIREITA,)
            tupla2 = (ABAIXO,)
            lista_acao_estadoatingido.append(tupla1)
            lista_acao_estadoatingido.append(tupla2)
        elif col == 2:  # direita; abaixo
            tupla1 = (DIREITA,)
            tupla2 = (ABAIXO,)
            lista_acao_estadoatingido.append(tupla1)
            lista_acao_estadoatingido.append(tupla2)

    return lista_acao_estadoatingido


def get_string_acao(lin, col, matriz, acao):
    aux = matriz[lin][col]
    if acao == DIREITA:
        matriz[lin][col] = matriz[lin][col + 1]
        matriz[lin][col + 1] = aux
    elif acao == ESQUERDA:
        matriz[lin][col] = matriz[lin][col - 1]
        matriz[lin][col - 1] = aux
    elif acao == ACIMA:
        matriz[lin][col] = matriz[lin - 1][col]
        matriz[lin - 1][col] = aux
    elif acao == ABAIXO:
        matriz[lin][col] = matriz[lin + 1][col]
        matriz[lin + 1][col] = aux

    return matriz_to_linha(matriz)


'''
    elif lin == 1:
        if col == 0:
            # acima; direita; abaixo
        elif col == 1:
            # esquerda; direita; abaixo
        elif col == 2:
            # esquerda; acima; abaixo
    elif lin == 2:
        if col == 0:
            # acima; direita
        elif col == 1:
            # esquerda; acima; direita
        elif col == 2:
            # esquerda; acima
            return
'''


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


'''========================================================================================='''
'''
class Estado:

    def funcao1(self):
        print('Estado')
        print('============')
        print('============')
'''
