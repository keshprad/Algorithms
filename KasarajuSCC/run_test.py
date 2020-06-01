from KasarajuSCC import SCC


def runSCC(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    Kasaraju = SCC.StronglyConnectedComponents(fileIn)

    print("\tinput = ", str(Kasaraju.graph))

    print("\tSize of 5 largest SCCs: ", Kasaraju.findSCC(), "\n")


#######################
runSCC("test1.txt")
runSCC("test2.txt")
runSCC("test3.txt")
runSCC("test4.txt")
runSCC("test5.txt")

# Long test cases
# runSCC("SCC.txt")
