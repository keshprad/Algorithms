from GreedyWeightedCompletionTimes import Scheduling


def runRunningMedians(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    greedyTime = Scheduling.completionTimes(fileIn)

    ratioTime, diffTime = greedyTime.findMinCompletionTimes()

    print("\tMinimum Weighted Completion Times:")
    print("\t\tWhen ordered decreasing with w - l: " + str(diffTime))
    print("\t\tOptimal time -> When ordered decreasing with w / l: " + str(ratioTime) + "\n")

#######################
runRunningMedians("test1.txt")
runRunningMedians("test2.txt")
runRunningMedians("test3.txt")
runRunningMedians("test4.txt")
runRunningMedians("test5.txt")
runRunningMedians("jobs.txt")