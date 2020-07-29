import time as t
from SimpleClustering import Cluster


def runClustering(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    c = Cluster.ClusterFinder(fileIn)

    start = t.time()
    c.findClusters()
    lap1 = t.time()
    spacing = c.findSpacing()
    end = t.time()

    print("\tTime to cluster: " + str(lap1-start))
    print("\tTime to find cluster spacing: " + str(end-lap1))
    print("\tResulting " + str(c.k) + "-clustering:")
    print("\t\t" + str(c.union_find.getGraph()))
    print("\tMax spacing of the " + str(c.k) + "-clustering: " + str(spacing) + "\n")


#######################
runClustering("test1.txt")
runClustering("test2.txt")
runClustering("test3.txt")
runClustering("test4.txt")
runClustering("test5.txt")
runClustering("clustering1.txt")
