class completionTimes:
    def __init__(self, filePath):
        self.weights, self.lengths = self.readFile(filePath)

    def readFile(self, filePath):
        fin = open(filePath)
        numJobs, weights, lengths = None, [], []

        for line in fin:
            if numJobs is None:
                numJobs = int(line)
            else:
                line = line.split()
                weights.append(int(line[0]))
                lengths.append(int(line[1]))
        return weights, lengths

    def findMinCompletionTimes(self):
        ratios = self.findRatios()
        sortedRatios = sorted(ratios, reverse=True)

        diffs = self.findDiffs()
        sortedDiffs = sorted(diffs, reverse=True)

        return self.findTime(ratios, sortedRatios), self.findTime(diffs, sortedDiffs)

    def findRatios(self):
        ratios = {}
        for i in range(len(self.weights)):
            if self.weights[i] / self.lengths[i] not in ratios:
                ratios[self.weights[i] / self.lengths[i]] = [i]
            else:
                ratios[self.weights[i] / self.lengths[i]].append(i)
        return ratios

    def findDiffs(self):
        diffs = {}
        for i in range(len(self.weights)):
            if self.weights[i] - self.lengths[i] not in diffs:
                diffs[self.weights[i] - self.lengths[i]] = [i]
            else:
                diffs[self.weights[i] - self.lengths[i]].append(i)
        return diffs

    def findTime(self, unordered, ordered):
        currLength, time = 0, 0

        for each in ordered:
            max_weights = {}
            for index in unordered[each]:
                max_weights[index] = self.weights[index]

            max_weights = {key: value for key, value in sorted(max_weights.items(), key=lambda x: x[1], reverse=True)}

            for index in max_weights:
                currLength += self.lengths[index]
                weight = max_weights[index]
                time += weight * currLength
        return time
