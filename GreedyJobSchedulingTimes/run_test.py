from GreedyJobSchedulingTimes import Scheduling


def runGreedyScheduling(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    greedyTime = Scheduling.completionTimes(fileIn)

    ratioTime, diffTime = greedyTime.findMinCompletionTimes()

    print("\tMinimum Weighted Completion Times:")
    print("\t\tWhen ordered decreasing with w - l: " + str(diffTime))
    print("\t\tOptimal time -> When ordered decreasing with w / l: " + str(ratioTime) + "\n")

#######################
runGreedyScheduling("test1.txt")
runGreedyScheduling("test2.txt")
runGreedyScheduling("test3.txt")
runGreedyScheduling("test4.txt")
runGreedyScheduling("test5.txt")
runGreedyScheduling("jobs.txt")