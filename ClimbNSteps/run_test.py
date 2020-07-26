from ClimbNSteps import climb_n_steps


def runClimbSteps(n, x):
    combos = climb_n_steps.find_step_combinations(n, x)
    print("There are " + str(combos) + " ways to climb up " + str(
        n) + " steps if at each move you can choose the number of steps from " + str(x) + "!")

######################
runClimbSteps(5, [1, 2])
runClimbSteps(7, [1, 3, 9])
runClimbSteps(100, [1, 9, 17])
runClimbSteps(1000, [1, 3, 29, 36, 69, 71, 100])