class Grafos:
    def __init__(self, vertex):
        self.vertex = vertex
        self.matrix = [[0 for x in range(vertex)] for y in range(vertex)]

    def addEdge(self,v1,v2):
        self.matrix[v1-1][v2-1] += 1
        if v1 != v2:
            self.matrix[v2-1][v1-1] += 1

    def show(self):
        for line in self.matrix:
            out = "|\t"
            for index in line:
                out = out + str(round(index)) + "\t"
            out = out + "|"
            print(out)

    def showDegrees(self):
        for index, line in enumerate(self.matrix):
            print(f'Vertice {index+1} - {int(sum(line))} graus')

    def maxDegree(self):
        return max(sum(line) for line in self.matrix)

    def minDegree(self):
        return min(sum(line) for line in self.matrix)