class InversionsCounter(object):
    def __init__(self):
        self.res = [];
        self.inversions = 0;

    def readResultFile(self, f = ""):
        if not f:
            return
        else:
            # open and read document to buffer:
            with open(f, "r") as p:
                for line in p:
                    return int(line)
            p.close()


    def readFile(self, f = ""):
        if not f:
            return
        else:
            # open and read document to buffer:
            with open(f, "r") as p:
                for line in p:
                    self.res.append(int(line))
            p.close()
            return self.res

    def sortAndCount(self, a):
        if (len(a) <= 1):
            return a
        left = self.sortAndCount(a[:len(a)//2])
        right = self.sortAndCount(a[len(a)//2:])

        return self.mergeAndCountSplits(left, right)

    def mergeAndCountSplits(self, left, right):
        out = []
        i = 0
        j = 0
        for k in range(len(left) + len(right)):
            if i >= len(left):
                out.append(right[j])
                j += 1
            elif j >= len(right):
                out.append(left[i])
                i += 1
            elif left[i] <= right[j]:
                out.append(left[i])
                i += 1
            elif left[i] > right[j]:
                out.append(right[j])
                j += 1
                self.inversions += len(left) - i
        self.res = out
        return out

