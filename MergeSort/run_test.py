from MergeSort import Inversions
def runInversions (fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    inv = Inversions.InversionsCounter()
    input = inv.readFile(fileIn)

    print("input = " + str(input))
    print("sorted = " + str(inv.sortAndCount(input)))
    print("inversions = " + str(inv.inversions) + "\n")


#######################
runInversions("finalCase.txt")
runInversions("test1.txt")
runInversions("test3.txt")
runInversions("test4.txt")
runInversions("test5.txt")
# runInversions("finalCase.txt") #Comment out when testing code. This file is just too damn long

