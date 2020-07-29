import time as t
from MergeSort import Inversions


def runInversions(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    inv = Inversions.InversionsCounter()
    input = inv.readFile(fileIn)

    print("input = " + str(input))
    start = t.time()
    sorted_list = inv.sortAndCount(input)
    end = t.time()
    print("Time to sort using MergeSort: " + str(end-start))
    print("sorted = " + str(sorted_list))
    print("inversions = " + str(inv.inversions) + "\n")


#######################
runInversions("test1.txt")
runInversions("test2.txt")
runInversions("test3.txt")
runInversions("test4.txt")
runInversions("test5.txt")
# runInversions("finalCase.txt") #Comment out when testing code. This file is just too damn long
