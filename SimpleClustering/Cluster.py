from UnionFind_DisjointSet import UnionFind


class ClusterFinder:
    def __init__(self, fileName):
        self.edgeCosts, self.vertices = self.readFile(fileName)
        self.union_find = UnionFind.UnionFind(self.vertices)

        self.k = float("inf")
        while self.k > self.union_find.currClusters:
            try:
                self.k = int(input("\tHow many clusters?"))
                if self.k > self.union_find.currClusters:
                    print("\tSelect Again! Make sure to select a valid integer between 1 and "
                          + str(self.union_find.currClusters) + " inclusive!\n")
            except ValueError:
                print("\tSelect Again! Make sure to select a valid integer between 1 and "
                      + str(self.union_find.currClusters) + " inclusive!\n")


    def readFile(self, fileName):
        edgeCosts, vertices = {}, []
        fin, numClusters = open(fileName), None

        for line in fin:
            line = line.split()

            if numClusters is None:
                numClusters = int(line[0])
            else:
                currEdge = [int(line[0]), int(line[1])]
                currCost = int(line[2])
                if currCost not in edgeCosts:
                    edgeCosts[currCost] = [currEdge]
                else:
                    edgeCosts[currCost].append(currEdge)

                if [currEdge[0]] not in vertices:
                    vertices.append([currEdge[0]])
                if [currEdge[1]] not in vertices:
                    vertices.append([currEdge[1]])
        return edgeCosts, vertices

    def findClusters(self):
        keys = list(sorted(self.edgeCosts.keys()))
        counter = 0

        while self.union_find.currClusters != self.k:
            currCost = keys[counter]
            counter += 1

            for edge in self.edgeCosts[currCost]:
                if self.union_find.currClusters == self.k:
                    break
                else:
                    vert1, vert2 = edge[0], edge[1]
                    self.union_find.union(vert1, vert2)

    def findSpacing(self):
        spacing = float('inf')
        for cost in self.edgeCosts:
            for edge in self.edgeCosts[cost]:
                if self.union_find.find(edge[0]) != self.union_find.find(edge[1]):
                    spacing = min(spacing, cost)
        return spacing
