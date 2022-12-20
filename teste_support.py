from modulo_estruturas import solucao as sol


if __name__ == "__main__":
    """Testes para método sucessor"""
    print('-------------------------------------------------')
    print('Chamada método: \"sucessor\": 2_3541687')
    lista_acoes = sol.sucessor('2_3541687')
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes)
    print('-------------------------------------------------')

    print('-------------------------------------------------')
    print('Chamada método: \"sucessor\": _23541687')
    lista_acoes = sol.sucessor('_23541687')
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes)
    print('-------------------------------------------------')




