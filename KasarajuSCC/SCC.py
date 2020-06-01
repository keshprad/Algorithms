import copy


class StronglyConnectedComponents:
    def __init__(self, filePath):
        self.graph, self.n = self.readFile(filePath)
        self.finishing_times = [-1] * len(self.graph)
        self.scc_sizes = []

    def readFile(self, filePath):
        fin, graph = open(filePath), {}

        for line in fin:
            line = line.split()
            key = int(line[0])
            n = 0

            if key > n:
                n = key
            if key not in graph:
                graph[key] = {'in': [], 'out': [], 'explored': False}
            for each in line[1:]:
                value = int(each)
                graph[key]['out'].append(value)
                if value > n:
                    n = value
                if value not in graph:
                    graph[value] = {'in': [], 'out': [], 'explored': False}
                graph[value]['in'].append(key)

        for each in range(1, n+1):
            if each not in graph.keys():
                graph[each] = {'in': [], 'out': [], 'explored': False}
        return graph, n

    def findSCC(self):
        self.DFS_Loop(True)
        self.graph = self.replaceFinishingTimes()
        self.DFS_Loop()
        return self.find5MaxSizes()

    time = 0

    def DFS(self, i, order):
        global time

        self.graph[i]['explored'] = True

        for each in self.graph[i][order]:
            if not self.graph[each]['explored']:
                self.DFS(each, order)

        time += 1

        if order == 'in':
            self.finishing_times[i - 1] = time

    def DFS_Loop(self, reversed=False):
        global time
        time = 0

        order = 'out'
        if reversed:
            order = 'in'

        for i in range(self.n, 0, -1):
            if not self.graph[i]['explored']:
                self.DFS(i, order)
                if order == 'out':
                    self.scc_sizes.append(time)
                    time = 0

    def replaceFinishingTimes(self):
        newGraph = {}

        for each in self.graph.keys():
            self.graph[each]['explored'] = False
            for order in ['in', 'out']:
                for i in range(len(self.graph[each][order])):
                    oldNode = self.graph[each][order][i]
                    self.graph[each][order][i] = self.finishing_times[oldNode - 1]
            newGraph[self.finishing_times[each - 1]] = self.graph[each]
        return newGraph

    def find5MaxSizes(self):
        sizes = copy.deepcopy(self.scc_sizes)
        max5sizes = []

        for i in range(5):
            if len(sizes) != 0:
                currMax = max(sizes)
                max5sizes.append(currMax)
                sizes.remove(currMax)
            else:
                break
        return max5sizes
