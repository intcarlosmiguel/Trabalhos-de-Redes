import wikipedia
import random

def generate(texto,neigh): # Gera aleatoriamente uma raiz

    texto = neigh[int(random.uniform(0, 1)*len(neigh))]
    return texto

def generatejson(tam):
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
        while((sitio,proximo) in sites and proximo == sitio):
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
        print(len(sites)-1,sitio,len(viz))
        viz = [i for i in link if i in vizinhoRaiz]
        if(len(viz)<=1):
            sitio = raiz
            neigh = vizinhoRaiz
            continue
        else:
            sitio = proximo
            neigh = viz
    return sites

if(__name__ == '__main__'):
    generatejson('data1.json',500)