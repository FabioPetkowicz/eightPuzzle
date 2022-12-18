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
    tree = Tree(1)
    tree.root.sun[0] = 0
    tree.root.sun[1] = 1
    tree.root.sun[2] = 2
    tree.root.sun[3] = 3
    ##n1 = Node(1)
    ##tree.root = n1

    print(tree.root)
    print(tree.root.sun[0])
    print(tree.root.sun[1])
    print(tree.root.sun[2])
    print(tree.root.sun[3])
