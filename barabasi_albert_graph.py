import networkx as nx
import matplotlib.pyplot as plt
from math import *
def barabasi_albert_graph (G, nNodes , mLinks):
    p = []
    x = len(G)
    for i in range(1,x+1):
        y = G.neighbors(i)
        z= len(y)
        p.append(1/z)
    p.sort()
    hola = p[-1]
    hola = 1/hola
    G.add_edge(hola,x+1)
    if(x+1 != nNodes):
        barabasi_albert_graph (G, nNodes , mLinks)
    G_new = G.copy()
    return G_new
if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1)
    G.add_node(2)
    G.add_edge(1,2)
    nx.draw(G)
    plt.show()
    G_new = barabasi_albert_graph (G,98,1)
    nx.draw(G_new)
    plt.show()