import support as sp

class Nodo:
    def __init__(self, estado = '', pai = None, acao = None, custo = 0):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __repr__(self):
        """override toString default python"""
        return '%s  %s %s %s' % (self.estado, self.pai, self.acao, self.custo)