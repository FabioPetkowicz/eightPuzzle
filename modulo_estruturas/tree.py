class Node:
    def __init__(self, data):
        self.data = data
        self.sun = [None, None, None, None]

    def __str__(self):
        return str(self.data)

    def sun(self, index):
        return self.sun[index]


class Tree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None




if __name__ == "__main__":
    tree = Tree()
    n1 = Node(1)
    tree.root = n1

    print(tree.root)

'''
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.imprime_pai_filhos()
    print('-----------------------------------')
    print('Valor do Nodo:', tree.root.__str__())
    print('Filho da Esquerda:', tree.root.left)
    print('Filho da Direita:', tree.root.right)
'''