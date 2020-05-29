from SelectIthOrderStatistic import Selection

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
runComparisons("5Nums.txt", 1)
runComparisons("5Nums.txt", 3)
runComparisons("5Nums.txt", 5)

runComparisons("20Nums.txt", 7)
runComparisons("20Nums.txt", 12)
runComparisons("20Nums.txt", 20)

runComparisons("100Nums.txt", 20)
runComparisons("100Nums.txt", 75)
runComparisons("100Nums.txt", 100)

runComparisons("1000Nums.txt", 5)
runComparisons("1000Nums.txt", 100)
runComparisons("1000Nums.txt", 976)