class comparisonCounter(object):
    def __init__(self):
        self.input = []
        self.res = []
        self.comparisons = 0;

    def reset(self):
        self.res = self.input.copy()
        self.comparisons = 0

    def readFile(self, f=""):
        if not f:
            return
        with open(f, "r") as p:
            for line in p:
                self.input.append(int(line))
        p.close()
        self.res = self.input.copy()
        return self.input

    def quickSort(self, l, r, pType):
        if l >= r:
            return
        if pType == 1:
            p = l
        elif pType == 2:
            p = r
        elif pType == 3:
            p = self.choose3MedianPivot(l, r)
        self.res[p], self.res[l] = self.res[l], self.res[p]
        p = self.partition(l, r)
        self.quickSort(l, p - 1, pType)
        self.quickSort(p + 1, r, pType)

    def partition(self, l, r):
        self.comparisons += r - l

        i = l
        for j in range(l + 1, r + 1):
            if self.res[j] < self.res[l]:
                i += 1
                self.res[j], self.res[i] = self.res[i], self.res[j]
        self.res[i], self.res[l] = self.res[l], self.res[i]
        return i

    def choose3MedianPivot(self, l, r):
        mid = (l + r) // 2
        if self.res[l] <= self.res[r] <= self.res[mid] or self.res[mid] <= self.res[r] <= self.res[l]:
            return r
        elif self.res[mid] <= self.res[l] <= self.res[r] or self.res[r] <= self.res[l] <= self.res[mid]:
            return l
        return mid