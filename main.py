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

'''
    no1 = sp.Nodo('estado1', 'pai1', 'acao1', 'custo1')
    print(no1.estado)
    print(no1)
    novo_estado = 's0'
    lista_tuplas_acao_estado = sp.sucessor(novo_estado)

    print('-------------------------------------------------')
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_tuplas_acao_estado)
    print('-------------------------------------------------')
'''
