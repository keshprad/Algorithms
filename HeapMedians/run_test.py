from HeapMedians import RunningMedians


def runRunningMedians(fileIn):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    Medians = RunningMedians.HeapMedians()

    Medians.findRunningMedians(fileIn)
    print("\tMedians after inserting each element:\n\t\t" + str(Medians.running_medians))

    total = sum(Medians.running_medians)
    print("\tsum of medians:", str(total))
    print("\tsum of medians % entries inserted:", str(total % len(Medians.running_medians)) + "\n")


#######################
runRunningMedians("test1.txt")
runRunningMedians("test2.txt")
runRunningMedians("test3.txt")
runRunningMedians("test4.txt")
runRunningMedians("test5.txt")
runRunningMedians("Median.txt")
