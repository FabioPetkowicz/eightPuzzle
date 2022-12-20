

ESQUERDA = 'esquerda'
ACIMA = 'acima'
DIREITA = 'direita'
ABAIXO = 'abaixo'
ESPACO_VAZIO = '_'

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
        return '%s  %s %s %s' % (self.estado, self.pai, self.acao, self.custo)

def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado: str
    :return: list
    """
    lista_de_tuplas = []
    posicao_vazio = estado.find(ESPACO_VAZIO)

    # ESQUERDA
    if posicao_vazio != 0 and posicao_vazio != 3 and posicao_vazio != 6:
        aux = estado
        temp_list = list(aux)
        temp_list[posicao_vazio] = temp_list[posicao_vazio - 1]
        temp_list[posicao_vazio - 1] = ESPACO_VAZIO
        aux = ''.join(temp_list)
        lista_de_tuplas.append((ESQUERDA, aux))

    # ACIMA
    if posicao_vazio != 0 and posicao_vazio != 1 and posicao_vazio != 2:
        aux = estado
        temp_list = list(aux)
        temp_list[posicao_vazio] = temp_list[posicao_vazio - 3]
        temp_list[posicao_vazio - 3] = ESPACO_VAZIO
        aux = ''.join(temp_list)
        lista_de_tuplas.append((ACIMA, aux))

    # DIREITA
    if posicao_vazio != 2 and posicao_vazio != 5 and posicao_vazio != 8:
        aux = estado
        temp_list = list(aux)
        temp_list[posicao_vazio] = temp_list[posicao_vazio + 1]
        temp_list[posicao_vazio + 1] = ESPACO_VAZIO
        aux = ''.join(temp_list)
        lista_de_tuplas.append((DIREITA, aux))

    # ABAIXO
    if posicao_vazio != 6 and posicao_vazio != 7 and posicao_vazio != 8:
        aux = estado
        temp_list = list(aux)
        temp_list[posicao_vazio] = temp_list[posicao_vazio + 3]
        temp_list[posicao_vazio + 3] = ESPACO_VAZIO
        aux = ''.join(temp_list)
        lista_de_tuplas.append((ABAIXO, aux))

    return lista_de_tuplas
