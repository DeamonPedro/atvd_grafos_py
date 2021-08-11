from Grafos import Grafos

size = int(input("digite o numero de vertices: "))
grafo = Grafos(size)
while True:
    res = str(input("adicionar aresta? [s/n]: "))
    if res.upper() == 'N':
        break
    v1 = int(input("vertice base: "))
    v2 = int(input("vertice alvo: "))
    grafo.addEdge(v1,v2)

grafo.show()
grafo.showDegrees()
print('maior grau =',grafo.maxDegree())
print('menor grau =',grafo.minDegree())