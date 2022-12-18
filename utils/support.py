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
    """"""
    ###estado é um string: ex: '_23541687'

    get_transicoes(estado)
    ##Cria a Lista de Tuplas
    lista = ['a', 'b', 'c']
    return lista


def get_transicoes(estado):
    ##avaliar as possibilidades de transição
    avalia_transicoes(linha_to_matriz(estado))


def avalia_transicoes(matriz):
    for i in range(len(matriz)):
        if matriz[i] == '_':
            return i  ##@doing now


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
