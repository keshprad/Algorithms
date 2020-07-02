class KnapsackProblem:
    def __init__(self, path):
        self.capacity, self.values, self.weights = self.read_file(path)

    def read_file(self, path):
        fin = open(path)
        capacity, num_items = None, None
        values, weights = [], []

        for line in fin:
            line = line.split()
            if capacity is None and num_items is None:
                capacity, num_items = int(line[0]), int(line[1])
            else:
                values.append(int(line[0]))
                weights.append(int(line[1]))
        return capacity, values, weights

    def maximize_value(self):
        graph = [[] for i in range(len(self.values))]

        for item in range(len(self.values)):
            for curr_weight in range(self.capacity + 1):
                if curr_weight < self.weights[item]:
                    if item == 0:
                        graph[item].append(0)
                    else:
                        graph[item].append(graph[item - 1][curr_weight])
                else:
                    if item == 0:
                        graph[item].append(self.values[item])
                    else:
                        value1 = self.values[item] + graph[item - 1][curr_weight - self.weights[item]]
                        value2 = graph[item - 1][curr_weight]
                        graph[item].append(max(value1, value2))
        return graph[len(self.values) - 1][self.capacity]
