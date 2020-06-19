class UnionFind:
    def __init__(self, clusterInput):
        # clusterInput is a 2d-Array of clusters
        self.graph = {}
        # ranks simply represents an upper bound on the tree level since they get offset by the path compression
        self.ranks = {}
        # amount of current clusters
        self.currClusters = len(clusterInput)

        for cluster in clusterInput:
            if len(cluster) > 0:
                parent = cluster[0]
                for each in cluster:
                    self.graph[each] = parent
                    self.ranks[each] = 0
                if len(cluster) > 1:
                    self.ranks[parent] = 1

    def addVertex(self, vertex, parent):
        self.graph[vertex] = parent

    def find(self, vertex):
        compress_list = [vertex]
        while vertex != self.graph[vertex]:
            vertex = self.graph[vertex]
            compress_list.append(vertex)

        if len(compress_list) > 2:
            compress_list = compress_list[:len(compress_list) - 2]
            self.pathCompression(compress_list, vertex)

        return vertex

    def union(self, vertex1, vertex2):
        parent1 = self.find(vertex1)
        parent2 = self.find(vertex2)

        if parent2 != parent1:
            if self.ranks[parent1] > self.ranks[parent2]:
                self.graph[parent2] = parent1
                self.ranks[parent1] = max(self.ranks[parent1], self.ranks[parent2] + 1)
            else:
                self.graph[parent1] = parent2
                self.ranks[parent2] = max(self.ranks[parent1] + 1, self.ranks[parent2])
            self.currClusters -= 1

    def pathCompression(self, compress_list, parent=None):
        # Assumes all vertices in compress_list have the same parent and that the list is not empty

        if parent is None:
            parent = self.find(compress_list[0])

        for vertex in compress_list:
            self.graph[vertex] = parent
