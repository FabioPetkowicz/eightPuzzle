from modulo_estruturas import solucao as sol
from modulo_estruturas.solucao import Nodo

ESTADO_1 = '2_3541687'
ESTADO_2 = '_23541687'
if __name__ == "__main__":
    """Testes para método sucessor"""
    print('-------------------------------------------------')
    print('Chamada método: \"sucessor\": ', ESTADO_1)
    lista_acoes1 = sol.sucessor(ESTADO_1)
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes1)
    print('-------------------------------------------------')

    print('-------------------------------------------------')
    print('Chamada método: \"sucessor\": ', ESTADO_2)
    lista_acoes2 = sol.sucessor(ESTADO_2)
    print('Imprimindo Lista de Tuplas Ação/Estado Atingido: ')
    print(lista_acoes2)
    print('-------------------------------------------------')

    ##__init__(self, estado='', pai=None, acao=None, custo=0)
    nodo = Nodo('2_3541687', None, None, 0)
    print(nodo)

    print('-------------------------------------------------')
    lista_de_nodos_sucessores = sol.sucessor(nodo.estado)

    for n in lista_de_nodos_sucessores:
        print('---------------')
        print(n)
        print('---------------')
