from UnionFind_DisjointSet import UnionFind
import random


class TestUnionFind:
    def __init__(self, clusterInput):
        self.clusterInput = clusterInput
        self.uf = UnionFind.UnionFind(clusterInput)
        print(self.uf.graph)

    def testUnion(self):
        keys = list(self.uf.graph.keys())
        vert1 = keys[random.randint(0, len(keys) - 1)]
        vert2 = keys[random.randint(0, len(keys) - 1)]
        print("Running union on", str(vert1), "and", str(vert2) + "...")

        self.uf.union(vert1, vert2)
        print(self.uf.graph)

    def testFind(self):
        keys = list(self.uf.graph.keys())
        vert1 = keys[random.randint(0, len(keys) - 1)]
        print("Running find on", str(vert1) + "...")

        print(self.uf.find(vert1))
        print(self.uf.graph)


#######################
clusterInput = [[1, 2, 3], [4], [5], [6, 7, 8, 9], [10], [11], [12, 13, 14, 15]]
testUF = TestUnionFind(clusterInput)

testUF.testUnion()
testUF.testFind()