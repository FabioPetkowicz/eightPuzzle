# -*- coding: utf-8 -*-
from modulo_estruturas import support as sp
import numpy as np

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

    a = np.array([1, 2, 3])
