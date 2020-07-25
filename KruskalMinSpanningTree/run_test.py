from KruskalMinSpanningTree import KruskalAlg


def runKruskalAlg(fileIn):
    print(fileIn + ":")

    # Use the same test cases as Prim's MST Alg. Allows us to compare the two
    fileIn = "../PrimMinSpanningTree/testCases/" + fileIn
    Kruskal = KruskalAlg.KruskalMST(fileIn)

    treeEdges, ovrCost = Kruskal.findMinSpanningTree()

    print("\tMinimum cost to span tree: " + str(ovrCost))
    print("\tTree Edges in the order spanned:")
    print("\t\t" + str(treeEdges) + "\n")


#######################
runKruskalAlg("test1.txt")
runKruskalAlg("test2.txt")
runKruskalAlg("test3.txt")
runKruskalAlg("test4.txt")
runKruskalAlg("test5.txt")
runKruskalAlg("edges.txt")
