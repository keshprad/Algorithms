# Given n(the number of steps on the staircase) and x(an array of the different possible steps you can take at a
# time) this function outputs the number of combinations you can go up the stairs

def find_step_combinations(n, x):
    if n == 0:
        return 1
    combos = [1] + ([None] * n)
    for curr_step in range(1, n + 1):
        num_combos = 0
        for i in x:
            if step >= i:
                num_combos += combos[curr_step - i]
        combos[curr_step] = num_combos
    return combos[n]
