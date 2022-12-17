import networkx as nx
G = nx.Graph()

# adicionando vertices
G.add_node(1)
G.add_node(2)

# Visualizando os vertices
print(G.nodes())

 #[1, 2]
'''
#adicionando arestas
G.add_edge(1, 2)
n_vertices = G.number_of_nodes()
n_arestas = G.number_of_edges()

print('vertices: ', n_vertices, '\narestas: ', n_arestas)
print(G.edges) # [(4, 5)]
'''