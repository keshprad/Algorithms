from RandomizedSelection import Selection

def runComparisons(fileIn, i):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    sel = Selection.randSelection()
    sel.readFile(fileIn)

    print("Using Randomized Selection algorithm to find the ith static in O(n) run time.")
    # Find ith static:
    print("\ti = " + str(i))
    print("\tinput = " + str(sel.res))
    sel.findIthStatistic(0, len(sel.input) - 1, i)
    print("\tith static = " + str(sel.ithStat))


#######################
runComparisons("test1.txt", 1)
runComparisons("test2.txt", 2)
# runComparisons("test3.txt")
# runComparisons("test4.txt")
# runComparisons("test5.txt")
# runComparisons("finalCase.txt")