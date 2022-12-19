#####################
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
        ##self.next = None

    def __repr__(self):
        return '%s  %s %s %s' % (self.estado, self.pai, self.acao, self.custo)

print('Hello Python')
no1 = Nodo('estado1', 'pai1', 'acao1', 'custo1')
print(no1.estado)