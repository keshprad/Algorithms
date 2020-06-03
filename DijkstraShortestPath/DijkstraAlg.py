class DijkstraShortestPath:
    def __init__(self, filePath):
        self.graph, self.minimums, self.path = self.readFile(filePath)

    def readFile(self, filePath):
        fin = open(filePath)
        graph, minimums, path = {}, {}, {}

        for line in fin:
            line = line.replace(',', ' ').split()
            key = int(line[0])
            graph[key], minimums[key], path[key] = [], float('inf'), ''

            counter = 0
            curr = []
            for each in line[1:]:
                curr.append(int(each))
                if counter % 2 == 1:
                    graph[key].append(curr)
                    curr = []
                counter += 1
        return graph, minimums, path

    def findShortestPaths(self, source=1):
        self.minimums[source] = 0
        self.path[source] = str(source)
        unvisited = list(self.minimums.keys())

        self.useDijkstra(source, unvisited)

    def useDijkstra(self, vertex, unvisited):
        # base case
        if len(unvisited) == 0 or vertex not in self.graph:
            return

        for each in self.graph[vertex]:
            adj_vertex = each[0]
            edge_length = each[1]

            if adj_vertex in unvisited:
                dist = self.minimums[vertex] + edge_length

                if self.minimums[adj_vertex] > dist:
                    self.minimums[adj_vertex] = dist
                    self.path[adj_vertex] = self.path[vertex] + ' -> ' + str(adj_vertex)

        unvisited.remove(vertex)
        self.useDijkstra(self.nextVertex(unvisited), unvisited)

    def nextVertex(self, unvisited):
        new_vertex = -1
        minimum = float('inf')
        for each in unvisited:
            if self.minimums[each] < minimum:
                new_vertex = each
                minimum = self.minimums[each]
        return new_vertex
