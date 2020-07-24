class GreedyKnapsackProblem:
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
        item_order = [(i, self.values[i] / self.weights[i]) for i in range(len(self.values))]
        item_order = sorted(item_order, key=lambda x: x[1], reverse=True)

        capacity_left, knap_value, knap_items = self.capacity, 0, []

        while capacity_left > 0 and item_order != []:
            item_number = item_order[0][0]
            knap_items.append(
                {"Item #": item_number, "weight": self.weights[item_number], "value": self.values[item_number]})

            if self.weights[item_number] <= capacity_left:
                capacity_left -= self.weights[item_number]
                knap_value += self.values[item_number]
                item_order = item_order[1:]
            else:
                percentage = capacity_left / self.weights[item_number]
                knap_value += percentage * self.values[item_number]
                capacity_left = 0
                item_order = item_order[1:]
        return knap_value, knap_items
