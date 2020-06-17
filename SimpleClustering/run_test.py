from SimpleClustering import Cluster


def runClustering(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    c = Cluster.ClusterFinder(fileIn)

    c.findClusters()
    spacing = c.findSpacing()

    print("\tResulting " + str(c.k) + "-clustering:")
    print("\t\t" + str(c.union_find.graph))
    print("\tMax spacing of the " + str(c.k) + "-clustering: " + str(spacing) + "\n")


#######################
runClustering("test1.txt")
runClustering("test2.txt")
runClustering("test3.txt")
runClustering("test4.txt")
runClustering("test5.txt")
runClustering("clustering1.txt")
