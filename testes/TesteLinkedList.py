from modulo_estruturas.LinkedList import LinkedList, Node

print('===============INICIO=====================')
no1 = Node(1)
no2 = Node(2)
print(no1)
print(no2)
print('=================================================')

lista = LinkedList()
print('Tamanho da Lista:', len(lista))

lista.append(10)
print('Tamanho Lista:', len(lista))
lista.append(20)
lista.append(30)
print('Tamanho Lista:', len(lista))

print('Elemento 0:', lista[0])
print('Elemento 1:', lista[1])
print('Elemento 2:', lista[2])

lista[2] = 3
print('Agora Elemento 2:', lista[2])

item_pos = lista.__getitem__(1)
print('Elemento posição 1:', item_pos)

print('Invalido. Lança Exceção...', lista[3])
