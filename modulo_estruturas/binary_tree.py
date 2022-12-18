class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def get_left_sun(self):
        return self.left

    def get_right_sun(self):
        return self.right


class BinaryTree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def imprime_pai_filhos(self):
        print('Valor do Nodo:', self.root.data)
        print('Filho da Esquerda:', self.root.get_left_sun())
        print('Filho da Direita:', self.root.get_right_sun())

    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print(f'({node}', end='')
            self.simetric_traversal(node.left)
            #print(node)
        if node.right:
            self.simetric_traversal(node.right)
            #print(node)
            print(f'{node})', end='')


if __name__ == "__main__":
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    tree.root = n2

    tree.simetric_traversal()
    print()

'''
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.imprime_pai_filhos()
    print('-----------------------------------')
    print('Valor do Nodo:', tree.root.__str__())
    print('Filho da Esquerda:', tree.root.left)
    print('Filho da Direita:', tree.root.right)
    '''