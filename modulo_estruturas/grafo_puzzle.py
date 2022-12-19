import support as sp
### @to_do_here
'''
Item (4):
Este deverá ser o nodo padrão para grafos no projeto
Adaptar ele a árvore quaternária
'''
class Nodo:
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo
        self.sun = [None, None, None, None]

    def __repr__(self):
        """override toString default python"""
        return '%s  %s %s %s' % (self.estado, self.pai, self.acao, self.custo)

    def sun(self, index):
        return self.sun[index]

class Grafo:
    def __init__(self, data=None):
        if data:
            nodo = Nodo(data)
            self.root = nodo
        else:
            self.root = None

print('-------------------------------------------------')
no1 = Nodo('estado1', None, 'acao1', 'custo1')
print(no1)
print(no1.estado)
print(no1.acao)
print(no1.custo)
novo_estado = '_23541687'
print('-------------------------------------------------')
### @to_do_here
lista_tuplas_acao_estado = sp.sucessor(novo_estado)