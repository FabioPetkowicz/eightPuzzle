from modulo_estruturas import support as sp

## string de teste básico: '2_3541687'
## string de teste:        '_23541687'
if __name__ == "__main__":
    matriz = sp.linha_to_matriz('2_3541687')
    sp.imprime_matriz(matriz)

    print('-------------------------------------------------')
    print('Chamada método: \"get_acoes\":')
    lista_acoes = sp.get_acoes(0, 1, matriz)
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes)
    print('-------------------------------------------------')

    print('-------------------------------------------------')
    print('Chamada método: \"sucessor\"')
    lista_acoes = sp.sucessor('2_3541687')
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes)
    print('-------------------------------------------------')

    print('-------------------------------------------------')
    print('Chamada método: \"sucessor\"')
    lista_acoes = sp.sucessor('_23541687')
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes)
    print('-------------------------------------------------')




