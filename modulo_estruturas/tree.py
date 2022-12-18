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
    '''
    tree = Tree(1)
    tree.root.sun[0] = 0
    tree.root.sun[1] = 1
    tree.root.sun[2] = 2
    tree.root.sun[3] = 3

    print(tree.root)
    print(tree.root.sun[0])
    print(tree.root.sun[1])
    print(tree.root.sun[2])
    print(tree.root.sun[3])
    '''
    tree2 = Tree([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    #tree2.root = -1 #para caso de arvore com inicialização nulla;
    #talves seja descartada essa hipótese, pois agora o importante é funcionar

    tree2.root.sun[0] = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    tree2.root.sun[1] = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    tree2.root.sun[2] = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    tree2.root.sun[3] = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    print('Nodo Root:', tree2.root)
    print('Filho Zero:', tree2.root.sun[0])
    print('Filho Um:', tree2.root.sun[1])
    print('Filho Dois:', tree2.root.sun[2])
    print('Filho Três:', tree2.root.sun[3])

