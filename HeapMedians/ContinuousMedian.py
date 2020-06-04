import heapq


class HeapMedians:
    def __init__(self):
        self.running_medians, self.max_heap, self.min_heap = [], [], []

    def findRunningMedians(self, filePath):
        median = None
        fin = open(filePath)

        for line in fin:
            item = int(line)
            if median is None:
                median = item
            else:
                median = self.insert(item, median)
                median = self.balance(median)
            self.running_medians.append(median)

    def insert(self, item, median):
        if item < median:
            heapq.heappush(self.max_heap, -1 * item)
        else:
            heapq.heappush(self.min_heap, item)
        return median

    def balance(self, median):
        if len(self.min_heap) - len(self.max_heap) == 2:
            heapq.heappush(self.max_heap, -1 * median)
            median = heapq.heappop(self.min_heap)

        elif len(self.max_heap) - len(self.min_heap) == 1:
            heapq.heappush(self.min_heap, median)
            median = -1 * heapq.heappop(self.max_heap)
        return median
