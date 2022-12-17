
# coding: utf-8
'''========================================================================================='''

def le_arquivo():
    '''Leitura do arquivo de Entrada'''
    linha = ''
    with open('input.txt', 'r') as arquivo:
        linha = arquivo.read()
    return linha


def linha_to_matriz(str_puzzle):
    '''Conversão do String para Matriz'''
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
    puzzle_string = ''
    for i in range(0, len(mtz_puzzle)):
        for j in range(0, len(mtz_puzzle[i])):
            puzzle_string += mtz_puzzle[i][j]

    print('====================')
    print('Matriz Reconvertida a Linha:')
    print(puzzle_string)
    print('====================')

##Conversão da Matriz para String


def imprime_matriz(matriz):
    print(matriz[0])
    print(matriz[1])
    print(matriz[2])

##Função de Impressão do Estado Atual da Matriz

##Função Sucessor
def sucessor(estado):
    ##avaliar as possibilidades de transição

    ##Cria a Lista de Tuplas
    lista = ['a', 'b', 'c']
    return lista

def expande(nodo):

    sucessor(nodo.estado)
    print(nodo.estado)
'''========================================================================================='''
class Nodo:
    '''construtor default python'''
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        ##self.next = None ##? right_sun, left_sun,... --> NOP

    '''toString default python'''
    def __repr__(self):
        return '%s  %s %s %s' % (self.estado, self.pai, self.acao, self.custo)
'''========================================================================================='''
'''
class Estado:

    def funcao1(self):
        print('Estado')
        print('============')
        print('============')
'''
'''==================MAIN=================='''
string_inicial = le_arquivo()
print('=================================================')
print('Hello Eight Puzzle')
print(string_inicial)
print('=================================================')

matriz = linha_to_matriz(string_inicial)
imprime_matriz(matriz)
matriz_to_linha(matriz)

no1 = Nodo('estado1', 'pai1', 'acao1', 'custo1')
print(no1.estado)
print(no1)
novo_estado = 's0'
lista_tuplas_acao_estado = sucessor(novo_estado)


print('-------------------------------------------------')
print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
print(lista_tuplas_acao_estado)
print('-------------------------------------------------')
import networkx as nx
G = nx.Graph()
G.add_node(1)
G.add_node(2)
print('Nodos incluidos: ', G.nodes())