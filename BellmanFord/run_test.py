from BellmanFord import bellman_ford


def run_BellmanFord(file_path, source):
    print(file_path + ":")

    file_path = "testCases/" + file_path
    bf = bellman_ford.BellmanFord(file_path)
    print(bf.bf_path(source))


#######################
run_BellmanFord("test1.txt", 1)
run_BellmanFord("test2.txt", 1)
run_BellmanFord("test3.txt", 1)
run_BellmanFord("test4.txt", 1)
run_BellmanFord("test5.txt", 1)
