import time as t
from PrimMinSpanningTree import PrimAlg


def runPrimAlg(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    start = t.time()
    Prim = PrimAlg.MinSpanningTree(fileIn)

    treeEdges, ovrCost = Prim.findMinSpanningTree()
    end = t.time()

    print("\tTime to run: " + str(end-start))
    print("\tMinimum cost to span tree: " + str(ovrCost))
    print("\tTree Edges in the order spanned:")
    print("\t\t" + str(treeEdges) + "\n")


#######################
runPrimAlg("test1.txt")
runPrimAlg("test2.txt")
runPrimAlg("test3.txt")
runPrimAlg("test4.txt")
runPrimAlg("test5.txt")
runPrimAlg("edges.txt")