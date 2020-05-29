from QuickSort import Comparisons


class randSelection(Comparisons.comparisonCounter):
    def __init__(self):
        self.input = []
        self.res = []
        self.ithStat = 0
        self.comparisons = 0

    def findIthStatistic(self, l, r, i):
        i -= 1
        if l == r and i == 0:
            self.ithStat = self.res[r]
            return
        else:
            pivot = self.choose3MedianPivot(l, r)
            self.res[pivot], self.res[l] = self.res[l], self.res[pivot]
            pivot = self.partition(l, r)

            if pivot == i:
                self.ithStat = self.res[pivot]
                return
            elif pivot > i:
                return self.findIthStatistic(l, pivot - 1, i + 1)
            elif pivot < i:
                return self.findIthStatistic(pivot + 1, r, i + 1)
