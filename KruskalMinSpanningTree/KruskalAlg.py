from UnionFind_DisjointSet import UnionFind

class KruskalMST:
    def __init__(self, fileIn):
        # c_components will be a Union Find data structure to make tracking connected components simple.
        # Allows us to think of connected components as clusters
        self.edges, self.c_components = self.read_file(fileIn)
        self.treeEdges = []

    def read_file(self, fileIn):
        fin = open(fileIn)
        numVertices, numEdges = None, None
        edges, c_components = [], []

        for line in fin:
            line = line.split()
            if numVertices is None and numEdges is None:
                numVertices = int(line[0])
                numEdges = int(line[1])
            else:
                node1, node2, weight = int(line[0]), int(line[1]), int(line[2])
                edges.append((node1, node2, weight))
                if [node1] not in c_components:
                    c_components.append([node1])
                if [node2] not in c_components:
                    c_components.append([node2])
        return edges, UnionFind.UnionFind(c_components)

    def findMinSpanningTree(self):
        sorted_edges, c_components, ovr_cost = self.sort_costs(), [], 0

        for edge in sorted_edges:
            if edge[0] != edge[1]:  # Don't count self-loops
                ccomp_headers = self.find_ccomp_headers(edge)

                # Adds the edge if it won't create a cycle
                if ccomp_headers[0] != ccomp_headers[1]:
                    self.treeEdges.append(edge)
                    self.c_components.union(edge[0], edge[1])
                    ovr_cost += edge[2]
        return self.treeEdges, ovr_cost

    def sort_costs(self, edges=None):
        if edges is None:
            return sorted(self.edges, key=lambda x: x[2])
        return sorted(edges, key=lambda x: x[2], reverse=True)

    def find_ccomp_headers(self, edge):
        parent1 = self.c_components.find(edge[0])
        parent2 = self.c_components.find(edge[1])
        edgeIsIn = [parent1, parent2]
        return edgeIsIn
