from DijkstraShortestPath import DijkstraAlg


def runDijkstra(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    Dijkstra = DijkstraAlg.DijkstraShortestPath(fileIn)

    print("\tinput = ", str(Dijkstra.graph) + '\n')

    Dijkstra.findShortestPaths()
    print("\tLength of shortest path from Vertex 1:\n\t\t", Dijkstra.minimums, "\n")
    print("\tShortest path from Vertex 1:\n\t\t", Dijkstra.path, "\n")

    ex_vertex = list(Dijkstra.minimums.keys())[-1]
    print("\tExample:")
    print("\t\tDistance from Vertex #1 to Vertex #" + str(ex_vertex) + " is " + str(Dijkstra.minimums[ex_vertex]))
    print("\t\tPath from Vertex #1 to Vertex #" + str(ex_vertex) + " is " + Dijkstra.path[ex_vertex] + "\n\n")


#######################
runDijkstra("test1.txt")
runDijkstra("test2.txt")
runDijkstra("test3.txt")
runDijkstra("test4.txt")
runDijkstra("test5.txt")
runDijkstra("DijkstraData.txt")
