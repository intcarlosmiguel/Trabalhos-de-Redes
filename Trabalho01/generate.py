import wikipedia
import urllib
import random
import json
from os import listdir

def generate(texto,sites,neigh): # Gera aleatoriamente uma raiz

    a = 0
    while(texto in sites):
        texto = neigh[int(random.uniform(0, 1)*len(neigh))]
        a+= 1
        if(a==100):
            return []
    return texto

def generatejson(file,tam):
    if(file not in listdir('./')):
        network = {}
        sites = []
        raiz = 'Electron'
        vizinhoRaiz = wikipedia.WikipediaPage(raiz).links

        network[raiz] = vizinhoRaiz
        sites.append(raiz)
        neigh = vizinhoRaiz
        texto = raiz
        #texto = generate(site,sites,neigh)
        while(len(network)<tam):
            texto = generate(texto,sites,neigh)
            try:
                link = wikipedia.WikipediaPage(texto).links
            except:
                texto = raiz
                neigh = vizinhoRaiz
                continue
            viz = [i for i in link if i in vizinhoRaiz]
            if(len(viz)<=1):
                texto = raiz
                neigh = vizinhoRaiz
                continue
            else:
                network[texto] = link
                sites.append(texto)
                neigh = viz
            print(len(network)-1,texto,len(viz))
        with open(file, 'w') as f:
            json.dump(network, f,ensure_ascii=False)
    else:
        print("Arquivo já foi gerado!")

if(__name__ == '__main__'):
    generatejson('data1.json',500)