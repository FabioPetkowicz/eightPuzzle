class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return 'Dado: %s -> Próximo: %s' % (self.data, self.next)

    def funcao(self):
        print('Teste')


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size += 1

    ##19 minutos
    def __len__(self):
        return self._size

    def get(self, index):
        pass

    def __getitem__(self):
        # a = lista[6]
        self.index

    def __setitem__(self, index, elem):
        #lista[5] = 9
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out of range')
