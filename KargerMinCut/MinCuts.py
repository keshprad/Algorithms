import random
import copy

class MinCuts:
    def __init__(self, filePath):
        self.allVertices = self.readInput(filePath)

    def readInput(self, filePath):
        fin = open(filePath)
        graph = {}
        for line in fin:
            adjacents = [int(each) for each in line.split()];

            # find key value
            key = adjacents[0]

            # Set graph
            graph[key] = adjacents[1:]
        return graph

    def getRandomEdge(self, graph):
        v1 = list(graph.keys())[random.randint(0, len(graph) - 1)]  # current vertex
        v2 = graph[v1][random.randint(0, len(graph[v1]) - 1)]  # adjacent vertex
        return v1, v2

    def restore(self, graph, v1, v2):
        # replace occurrences of v2 with v1
        for each in graph[v2]:
            for j in range(len(graph[each])):
                if graph[each][j] == v2:
                    graph[each][j] = v1

        # get rid of self loops
        while v1 in graph[v1]:
            graph[v1].remove(v1)

        # removing the vertex after it has been combines
        del graph[v2]
        return graph

    def KargerMinCut(self, graph=None):
        if graph is None:
            graph = copy.deepcopy(self.allVertices)

        while len(graph) > 2:
            v1, v2 = self.getRandomEdge(graph)

            # add adjacent of the adjacent to the randVertexes, adjacent
            graph[v1].extend(graph[v2])

            # fix inconsistencies after extending the adjacent lists
            graph = self.restore(graph, v1, v2)
        return len(graph[list(graph.keys())[0]])
