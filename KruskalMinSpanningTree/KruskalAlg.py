class KruskalMST:
    def __init__(self, fileIn):
        self.edges = self.read_file(fileIn)
        self.treeEdges = []

    def read_file(self, fileIn):
        fin = open(fileIn)
        numVertices, numEdges = None, None
        edges = []

        for line in fin:
            line = line.split()
            if numVertices is None and numEdges is None:
                numVertices = int(line[0])
                numEdges = int(line[1])
            else:
                edges.append((int(line[0]), int(line[1]), int(line[2])))
        return edges

    def findMinSpanningTree(self):
        sorted_edges, c_components, ovr_cost = self.sort_costs(), [], 0

        for edge in sorted_edges:
            if edge[0] != edge[1]:  # Don't count self-loops
                edgeIsIn = self.checkCycles(c_components, edge)

                # Adds the edge if the edge doesn't create a cycle
                if len(edgeIsIn) != 2 or edgeIsIn[0] != edgeIsIn[1]:
                    self.treeEdges.append(edge)
                    ovr_cost += edge[2]

                # Each case where the edge doesn't cause a cycle
                if len(edgeIsIn) == 2:
                    # If the edge spans 2 connects 2 initially disconnected components
                    if edgeIsIn[0] != edgeIsIn[1]:
                        c_components[edgeIsIn[0]] += c_components[edgeIsIn[1]]
                        c_components = c_components[:edgeIsIn[1]] + c_components[edgeIsIn[1] + 1:]
                elif len(edgeIsIn) == 1:
                    # If one edge or the other is in a connected component, while others aren't
                    if edge[0] in c_components[edgeIsIn[0]]:
                        c_components[edgeIsIn[0]].append(edge[1])
                    if edge[1] in c_components[edgeIsIn[0]]:
                        c_components[edgeIsIn[0]].append(edge[0])
                elif len(edgeIsIn) == 0:
                    # None of the edges are in a connected component
                    c_components.append([edge[0], edge[1]])
        return self.treeEdges, ovr_cost

    def sort_costs(self, edges=None):
        if edges is None:
            return sorted(self.edges, key=lambda x: x[2])
        return sorted(edges, key=lambda x: x[2], reverse=True)

    def checkCycles(self, c_components, edge):
        edgeIsIn = []
        for i in range(len(c_components)):
            if edge[0] in c_components[i]:
                edgeIsIn.append(i)
            if edge[1] in c_components[i]:
                edgeIsIn.append(i)
        return edgeIsIn
