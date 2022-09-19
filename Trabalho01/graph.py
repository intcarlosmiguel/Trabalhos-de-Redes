import networkx as nx
import numpy as np
import json
import matplotlib.pyplot as plt

def read_json_file(filename):
    with open(filename) as f:

        data = json.load(f)
        G = nx.DiGraph()
        G.add_nodes_from([i for i in data])

        net = list(data.keys())
        lig = []
        for i in range(len(net)):
            site = net[i]
            for j in net[:i]:
                if(j in data[site]):
                    lig.append((site,j))
            for j in net[i+1:]:
                if(site in data[j]):
                    lig.append((j,site))
        G.add_edges_from(lig)

        return G

def hist_graph(G,name):
    if(name =='out'):
        return np.unique(np.array([G.out_degree[i] for i in G.nodes]),return_counts=True)
    else:
        return np.unique(np.array([G.in_degree[i] for i in G.nodes]),return_counts=True)

def metrics(G):
    print('Densidade da rede é:',nx.density(G))
    try:
        print(nx.diameter(G))
    except:
        print("Rede pouco densa, portanto encontramos um diâmetro infinto")
    print('Agrupamento da rede é de:',nx.transitivity(G))
    print('Reciprocidade da rede é de:',nx.reciprocity(G))

def sorting(s1,s2):
    s1_ = s2.argsort()
    s1 = s1[s1_[::-1]]
    s2 = s2[s1_[::-1]]
    return s1,s2

def degree(G,name):
    if(name =='out'):
        S = np.array([[i,G.out_degree[i]] for i in G.nodes]).T
    if(name=='in'):
        S = np.array([[i,G.in_degree[i]] for i in G.nodes]).T
    s1,s2 = sorting(S[0],S[1].astype(int))
    return s1,s2

def save_graph(G):
    nx.write_gpickle(G, "rede.gpickle")

def figure_hist(G,name,titulo):
    name,out = hist_graph(G,name)
    plt.figure(figsize=(8,8))
    plt.title(titulo)
    plt.xlabel("Grau do Nó")
    plt.ylabel("Quantidade de vezes que se repete")
    plt.xlim(-1,50)
    plt.bar(name,out,color = 'teal')
    plt.savefig("./out.jpg")
    plt.show()

def draw_graph(G):
    plt.figure(figsize=(8,8))
    plt.title('Rede da Wikipedia')
    nx.draw_kamada_kawai(G,with_labels=False,node_size = 50,alpha = 0.5,width = 0.5)
    plt.savefig("./network.jpg")
    plt.show()