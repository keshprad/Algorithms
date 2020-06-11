from PrimMinSpanningTree import PrimAlg


def runPrimAlg(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    Prim = PrimAlg.MinSpanningTree(fileIn)

    treeEdges, ovrCost = Prim.findMinSpanningTree()

    print("\tMinimum cost to span tree: " + str(ovrCost))
    print("\tTree Edges in the order spanned:")
    print("\t\t" + str(treeEdges) + "\n")


#######################
runPrimAlg("test1.txt")
runPrimAlg("test2.txt")
runPrimAlg("test3.txt")
runPrimAlg("test4.txt")
# runPrimAlg("test5.txt")
# commented because of test-case length
runPrimAlg("edges.txt")