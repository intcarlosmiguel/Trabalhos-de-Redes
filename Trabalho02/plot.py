import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.image as mpimg
import os
import json
from networkx.algorithms import community as cm


def greedy_algorithm(G):
    if('greedy.json' not in os.listdir('./community/')):
        greedy = cm.greedy_modularity_communities(G)
        greedy = {j:list(i) for i,j in zip(greedy,range(len(greedy)))}
        with open('./community/greedy.json', 'w') as f:
            json.dump(greedy, f)
    else:
        f = open('./community/greedy.json')
        greedy = json.load(f)
        return greedy


def newman_algorithm(G):
    if('newman.json' not in os.listdir('./community/')):
        newman = cm.girvan_newman(G)
        newman = list(newman)
        newman = {j:list(i) for i,j in zip(newman,range(len(newman)))}
        with open('./community/newman.json', 'w') as f:
            json.dump(newman, f)
    else:
        f = open('./community/newman.json')
        newman = json.load(f)
        return newman

def MMQ(x,y):
    m = (np.dot(x - np.mean(x),y - np.mean(y)))/(np.dot(x - np.mean(x),x - np.mean(x)))
    n = np.mean(y) - m*np.mean(x)
    r2 = 1 - (np.dot(y - (x*m + n),y - (x*m + n)))/(np.dot(y - np.mean(y),y - np.mean(y)))
    return m,n,r2
def degree_graph(G):
    degree = np.array(nx.degree_histogram(G)[1:])
    x = np.array(range(1,len(degree)+1))
    x = x[degree > 0]
    degree = degree[degree > 0]

    fig,ax = plt.subplots(figsize = (16,10),dpi = 500)
    ax.bar(x,degree,color = 'rebeccapurple')
    ax.set_xlim(1.5,50)
    ax.set_title('Histograma de Grau')
    ax.set_xlabel('Grau')
    ax.set_ylabel('Frequência')

    axins = ax.inset_axes([0.5, 0.5, 0.49, 0.49])

    logx = np.log(x)
    logdegree = np.log(degree)
    logdegree = logdegree[logx>2]
    logx = logx[logx>2]
    m,n,r2 = MMQ(logx[:40],logdegree[:40])
    y = m*logx + n

    axins.scatter(
        logx,
        logdegree,
        label = 'Histograma em Log vs Log',
        alpha = 0.6,
        color = 'navy'
    )
    axins.plot(
        logx,
        y,
        color = 'firebrick',
        label = 'Regressão com coeficiente: {m:.3}'.format(m=m),
    )
    axins.set_xticks([])
    axins.set_xlim(2.0,4.5)
    axins.set_yticks([])
    axins.legend()
    plt.savefig('./fig/degree.jpg')
    plt.show()