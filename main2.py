from modulo_estruturas.LinkedList import LinkedList,Node
##from modulo_estruturas.LinkedList import Node
import teste

'''===================================='''
teste.funcao()
print('===============INICIO=====================')

no1 = Node(1)
print(no1)

lista = LinkedList()
print('Tamanho da Lista: ', lista._size)

lista.append(10)
print(lista._size)
lista.append(20)
lista.append(30)
print(lista._size)

