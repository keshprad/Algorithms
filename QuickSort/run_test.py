import time as t
from QuickSort import Comparisons

def runComparisons(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    compare = Comparisons.comparisonCounter()
    compare.readFile(fileIn)

    # Leftmost pivot
    compare.reset()
    print("using leftmost pivot:")
    print("\tinput = " + str(compare.res))
    start = t.time()
    compare.quickSort(0, len(compare.input) - 1, 1)
    end = t.time()
    print("\tTime to sort using QuickSort: " + str(end-start))
    print("\tsorted = " + str(compare.res))
    print("\tcomparisons = " + str(compare.comparisons))

    # Rightmost Pivot
    compare.reset()
    print("using rightmost pivot:")
    print("\tinput = " + str(compare.res))
    start = t.time()
    compare.quickSort(0, len(compare.input) - 1, 2)
    end = t.time()
    print("\tTime to sort using QuickSort: " + str(end-start))
    print("\tsorted = " + str(compare.res))
    print("\tcomparisons = " + str(compare.comparisons))

    # Median-of-3 Pivot
    compare.reset()
    print("using median-of-3 pivot:")
    print("\tinput = " + str(compare.res))
    start = t.time()
    compare.quickSort(0, len(compare.input) - 1, 3)
    end = t.time()
    print("\tTime to sort using QuickSort: " + str(end-start))
    print("\tsorted = " + str(compare.res))
    print("\tcomparisons = " + str(compare.comparisons) + "\n")


#######################
runComparisons("test1.txt")
runComparisons("test2.txt")
runComparisons("test3.txt")
runComparisons("test4.txt")
runComparisons("test5.txt")
runComparisons("finalCase.txt")