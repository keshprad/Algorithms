from FloydWarshallShortestPath import floyd_warshall


def run_FloydWarshall(file_path):
    print(file_path + ":")
    file_path = "testCases/" + file_path

    fw = floyd_warshall.FloydWarshall(file_path)
    res = fw.floyd_warshall()
    if not res:
        print("\tCannot find shortest distances. Graph contains negative cycles.")
    else:
        print("\tAll Pairs Shortest Paths: " + "min = " + str(min([min(row) for row in res])))
        for row in res:
            print("\t" + str(row))


#######################
run_FloydWarshall("test1.txt")
run_FloydWarshall("test2.txt")
run_FloydWarshall("test3.txt")
