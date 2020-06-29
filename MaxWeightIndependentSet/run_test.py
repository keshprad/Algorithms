from MaxWeightIndependentSet import mwis


def runMWIS (fileIn, test_vertices=None):
    print(fileIn + ":")

    fileIn = "testCases/" + fileIn
    mwis_finder = mwis.MWIS(fileIn)

    result_set = mwis_finder.mwis()
    print("\tVertex numbers in the mwis: " + str(result_set))


    if test_vertices is None:
        test_vertices = [1, 2, 3, 4, 17, 117, 517, 997]
    print("\n\tTesting if the following vertices are in the mwis...")
    print("\ttest_vertices = " + str(test_vertices))

    test_bits = ""
    for vert in test_vertices:
        test_bits = test_bits + str(int(vert in result_set))
    print('\tresults: ' + test_bits + '\n\n')


#######################
runMWIS("test1.txt")
runMWIS("test2.txt")
runMWIS("test3.txt")
runMWIS("test4.txt")
runMWIS("test5.txt")
runMWIS("mwis.txt")
