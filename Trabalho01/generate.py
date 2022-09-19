import wikipedia
import urllib
import random
import json
from os import listdir

def getWikipedia(url):
    link = wikipedia.WikipediaPage(url).links

    return url,link

def generate(texto,sites,neigh):
    while(texto in sites):
        texto = neigh[int(random.uniform(0, 1)*len(neigh))]
    return texto

def generatejson(file,tam):
    print()
    if('data.json' not in listdir('./')):
        original = 'https://en.wikipedia.org/wiki/Special:Random'
        network = {}
        sites = []
        texto = urllib.request.urlopen(original).geturl().split("/wiki/")[1]
        while(len(network)<tam):
            try:
                site,neigh = getWikipedia(texto)
            except:
                texto = generate(site,sites,neigh)
                continue
                
            network[site] = neigh

            sites.append(site)
            texto = generate(site,sites,neigh)
            
            print(len(network),site)
        with open(file, 'w') as f:
            json.dump(network, f,ensure_ascii=False)
    else:
        print("Arquivo já foi gerado!")

if(__name__ == '__main__'):
    generatejson('data.json',500)