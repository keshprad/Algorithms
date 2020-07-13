class BellmanFord:
    def __init__(self, file_path):
        self.numVertices, self.edges = self.read_file(file_path)

    def read_file(self, file_path):
        fin = open(file_path)
        numVertices = None
        edges = []

        for line in fin:
            line = line.split()
            if numVertices is None:
                numVertices = int(line[0])
            else:
                tail, head, weight = int(line[0]), int(line[1]), int(line[2])
                edges.append([tail-1, head-1, weight])
        return numVertices, edges

    def bf_path(self, source=1):
        source -= 1

        min_dists = [float("inf")] * self.numVertices
        min_dists[source] = 0
        lastVertex = [None] * self.numVertices

        for i in range(self.numVertices - 1):
            for edge in self.edges:
                tail, head, weight = edge[0], edge[1], edge[2]
                if min_dists[tail] + weight < min_dists[head]:
                    min_dists[head] = min_dists[tail] + weight
                    lastVertex[head] = tail

        for edge in self.edges:
            tail, head, weight = edge[0], edge[1], edge[2]
            if min_dists[tail] + weight < min_dists[head]:
                return "Cannot find shortest distances. Graph contains negative weight cycle."

        result = "Vertex distance from the source(Vertex #{})".format(source+1)
        for i in range(self.numVertices):
            result += "\n\tVertex #{}: {}".format(i+1, min_dists[i])
        return result
