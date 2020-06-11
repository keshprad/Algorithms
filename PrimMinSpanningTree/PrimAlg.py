class MinSpanningTree:
    def __init__(self, fileIn):
        self.edges, self.costs = self.readFile(fileIn)
        self.treeEdges = []

    def readFile(self, fileIn):
        fin = open(fileIn)
        numVertices, numEdges = None, None
        edges, costs = {}, {}
        counter = 0

        for line in fin:
            line = line.split()
            if numVertices is None and numEdges is None:
                numVertices = int(line[0])
                numEdges = int(line[1])
            else:
                edges[counter] = [int(line[0]), int(line[1])]
                costs[counter] = int(line[2])
            counter += 1
        return edges, costs

    def findMinSpanningTree(self):
        lowestCosts = self.sortCosts()
        lowestInd = next(iter(lowestCosts))

        visited = [self.edges[lowestInd][0], self.edges[lowestInd][1]]
        unvisited = self.findUnvisted(visited)

        treeEdges = [self.edges[lowestInd]]
        ovrCost = self.costs[lowestInd]

        while len(unvisited) != 0:
            for i in lowestCosts:
                edge = self.edges[i]
                if (edge[0] in visited and edge[1] in unvisited) or (edge[1] in visited and edge[0] in unvisited):
                    treeEdges.append(edge)
                    ovrCost += lowestCosts[i]
                    if edge[1] in unvisited:
                        unvisited.remove(edge[1])
                        visited.append(edge[1])
                    else:
                        unvisited.remove(edge[0])
                        visited.append(edge[0])
                    break
        return treeEdges, ovrCost

    def sortCosts(self):
        return {key: value for key, value in sorted(self.costs.items(), key=lambda x: x[1])}

    def findUnvisted(self, visited):
        unvisited = []
        for edge in self.edges.values():
            for node in edge:
                if node not in visited and node not in unvisited:
                    unvisited.append(node)
        return unvisited