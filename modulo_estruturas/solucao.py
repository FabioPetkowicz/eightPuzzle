OBJETIVO = '12345678_'
ESQUERDA = 'esquerda'
ACIMA = 'acima'
DIREITA = 'direita'
ABAIXO = 'abaixo'
ESPACO_VAZIO = '_'


class Nodo:
    def __init__(self, estado=str, pai=None, acao=None, custo=0):
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
        return 'Ação: %s \nEstado: %s\nPai: %s \nCusto: %s' % (self.acao, self.estado, self.pai, self.custo)


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


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return: lista_de_nodos
    """
    lista_de_nodos = []
    l = sucessor(nodo.estado)

    for tupla in l:
        aux = Nodo(tupla[1], nodo, tupla[0], nodo.custo + 1)
        lista_de_nodos.append(aux)

    return lista_de_nodos


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    @param: str
    @return: str or None
    """
    if not eh_solucionavel(estado):
        return None
    else:
        X = set()
        F = dict()
        caminho = []
        estado_inicial = Nodo(estado)

        F[estado_inicial.estado] = estado_inicial

        while F != {}:
            v = F.popitem()[1]

            if v.estado == OBJETIVO:
                aux = v
                while aux.pai is not None:
                    caminho.insert(0, aux.acao)
                    aux = aux.pai
                return caminho

            if v.estado not in X:
                X.add(v.estado)
                vizinhos = expande(v)
                for vizinho in vizinhos:
                    F[vizinho.estado] = vizinho

    return None


def eh_solucionavel(estado):
    """ recebe um estado e retorna true se o estado possui solução ou false se não tem solução
        @param: str
        @return: bool
    """
    total_inv = conta_inversores([j for sub in estado for j in sub])

    return (total_inv % 2) == 0


def conta_inversores(estado):
    total_inv = 0
    for i in range(0, 9):
        for j in range((i + 1), 9):
            if estado[i] != ESPACO_VAZIO and estado[j] != ESPACO_VAZIO and estado[i] > estado[j]:
                total_inv += 1

    return total_inv
