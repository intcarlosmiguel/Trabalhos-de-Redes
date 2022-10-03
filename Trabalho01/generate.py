import wikipedia
import random
import networkx as nx
from graph import *
import os.path

def generate(texto,neigh): # Gera aleatoriamente uma raiz

    texto = neigh[int(random.uniform(0, 1)*len(neigh))]
    return texto

def generate_rede(tam):
    if not os.path.isfile('./rede.gpickle'):
        sites = []

        #Gera uma raiz
        raiz = 'Electron'
        vizinhoRaiz = wikipedia.WikipediaPage(raiz).links

        #Inicia a Rede
        neigh = vizinhoRaiz
        sitio = raiz

        while(len(sites)<tam):
            proximo = generate(sitio,neigh)
            a = 0
            while((sitio,proximo) in sites or proximo == sitio):
                proximo = generate(sitio,neigh)
                a+= 1
                if(a==100):
                    break
            if(a==100):
                sitio = raiz
                neigh = vizinhoRaiz
                continue
            try:
                link = wikipedia.WikipediaPage(proximo).links
            except:
                sitio = raiz
                neigh = vizinhoRaiz
                continue
            sites.append((sitio,proximo))
            viz = [i for i in link if i in vizinhoRaiz]
            print(len(sites),sitio)
            if(len(viz)<=1):
                sitio = raiz
                neigh = vizinhoRaiz
                continue
            else:
                sitio = proximo
                neigh = viz
        G = nx.DiGraph()
        G.add_edges_from([i for i in sites])
        save_graph(G)
    else:
        G = nx.read_gpickle("rede.gpickle")
    return G