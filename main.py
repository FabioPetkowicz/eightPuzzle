# -*- coding: utf-8 -*-
from utils import support as sp

def le_arquivo():
    '''Leitura do arquivo de Entrada'''
    linha = ''
    with open('input.txt', 'r') as arquivo:
        linha = arquivo.read()
    return linha


'''==================MAIN=================='''
if __name__ == "__main__":
    string_inicial = le_arquivo()
    print('=================================================')
    print('Hello Eight Puzzle: ', string_inicial)
    print('=================================================')

    matriz = sp.linha_to_matriz(string_inicial)
    sp.imprime_matriz(matriz)

    str_result = sp.matriz_to_linha(matriz)
    print('==========================================')
    print('Matriz convertida a linha: ', str_result)
    print('==========================================')

    print('-------------------------------------------------')
    print('Chamada método: \"sucessor\"')
    lista_acoes = sp.sucessor('2_3541687')
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes)
    print('-------------------------------------------------')
'''
    print('-------------------------------------------------')
    print('Chamada método: \"get_acoes\":')
    lista_acoes = sp.get_acoes(0, 1, matriz)
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes)
    print('-------------------------------------------------')
'''


'''
    no1 = sp.Nodo('estado1', 'pai1', 'acao1', 'custo1')
    print(no1.estado)
    print(no1)
    novo_estado = 's0'
    lista_tuplas_acao_estado = sp.sucessor(novo_estado)
'''