from Knapsack01 import knapsack

def run_knapsack01 (file):
    print(file + ":")
    file = "testCases/" + file

    knap = knapsack.KnapsackProblem(file)

    max_value = knap.maximize_value()
    print("\tMaximized value with weight less than knapsack capacity: " + str(max_value))


#######################
run_knapsack01("test1.txt")
run_knapsack01("test2.txt")
run_knapsack01("test3.txt")
run_knapsack01("test4.txt")
run_knapsack01("test5.txt")
run_knapsack01("knapsack1.txt")
