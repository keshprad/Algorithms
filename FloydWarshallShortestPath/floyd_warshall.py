class FloydWarshall:
    def __init__(self, file_path):
        self.num_vertices, self.pair_dists = self.read_file(file_path)

    def read_file(self, file_path):
        pair_dists, num_vertices = [], None

        fin = open(file_path)
        for line in fin:
            line = line.split()
            if num_vertices is None:
                num_vertices = int(line[0])

                # Create the initial matrix
                for i in range(num_vertices):
                    row = []
                    for j in range(num_vertices):
                        if i == j:
                            row.append(0)
                        else:
                            row.append(float("inf"))
                    pair_dists.append(row)
            else:
                tail, head, weight = int(line[0]) - 1, int(line[1]) - 1, int(line[2])
                pair_dists[tail][head] = weight
        return num_vertices, pair_dists

    def floyd_warshall(self):
        for k in range(self.num_vertices):
            curr_dist = [[None] * self.num_vertices for i in range(self.num_vertices)]
            for tail in range(self.num_vertices):
                for head in range(self.num_vertices):
                    curr_dist[tail][head] = min(self.pair_dists[tail][head],
                                                self.pair_dists[tail][k] + self.pair_dists[k][head])
            self.pair_dists = curr_dist

        # Check for negative cycles
        for i in range(self.num_vertices):
            if self.pair_dists[i][i] < 0:
                return False
        return self.pair_dists

    def print_results(self):
        result = "All Pairs Shortest Paths"
        for tail in range(self.num_vertices):
            for head in range(self.num_vertices):
                result += "\n" + str(tail+1) + " -> " + str(head+1) + ": " + str(self.pair_dists[tail][head])
        return result
