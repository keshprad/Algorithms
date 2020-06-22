from KargerMinCut import MinCuts


def runKarger(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    Karger = MinCuts.MinCuts(fileIn)

    print("input = " + str(Karger.allVertices))

    minCuts = 100000000000000000
    numTrials = 50
    for i in range(numTrials):
        cut = Karger.KargerMinCut()
        if cut < minCuts:
            minCuts = cut
        print('trial #{}:'
              '\n\t'
              'current min-cuts: {}'.format(i + 1, minCuts))
    print("\nAfter %s trials, # of min-cuts: %s" % (numTrials, minCuts))


#######################
runKarger("test1.txt")
runKarger("test2.txt")
runKarger("test3.txt")

# Long test cases; Uncomment as necessary
# runKarger("test4.txt")
# runKarger("test5.txt")
# runKarger("finalCase.txt")
