from GreedyKnapsack import greedy_knapsack

def run_greedy_knapsack (file):
    print(file + ":")
    file = "testCases/" + file

    knap = greedy_knapsack.GreedyKnapsackProblem(file)

    max_value, items = knap.maximize_value()
    print("\tMaximized value with weight less than knapsack capacity: " + str(max_value))
    print("\tItems in the max value knapsack: " + str(items))


#######################
run_greedy_knapsack("test1.txt")
run_greedy_knapsack("test2.txt")
run_greedy_knapsack("test3.txt")
run_greedy_knapsack("test4.txt")
run_greedy_knapsack("test5.txt")
