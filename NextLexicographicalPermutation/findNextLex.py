class nextLexPermutation:
    def findNextLexicographical(self, w=None):
        if w is None:
            w = input()
        w = list(w)
        l = self.findSuffix(w)

        # This means there are no lexicographically greater orderings
        if l == 0:
            return "no answer"

        w = self.swapPivot(w, l)
        return "".join(w)

    def findSuffix(self, w):
        # Finds non-increasing suffix
        l = len(w) - 1
        while l > 0 and w[l - 1] >= w[l]:
            l -= 1
        return l

    def swapPivot(self, w, l):
        # Find RIGHTMOST successor to pivot
        pivot, r = l - 1, len(w) - 1
        while w[pivot] >= w[r]:
            r -= 1
        w[pivot], w[r] = w[r], w[pivot]

        # Reverse suffix
        w[l:] = w[:pivot: -1]
        return w