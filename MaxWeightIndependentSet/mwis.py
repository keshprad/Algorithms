class MWIS:
    def __init__(self, filePath):
        self.weights = self.readFile(filePath)

    def readFile(self, filePath):
        fin = open(filePath)
        weights = [int(line) for line in fin]
        return weights[1:]

    def mwis(self):
        res = self.find_mwis()
        ans = self.reconstruct_set(res)
        return ans

    def find_mwis(self):
        res = [0, self.weights[0]]
        for z in range(2, len(self.weights) + 1):
            new = max(res[z-1], res[z-2] + self.weights[z-1])
            res.append(new)
        return res

    def reconstruct_set(self, res):
        mwis = []
        z = len(res) - 1
        while z > 1:
            if res[z - 1] >= res[z - 2] + self.weights[z - 1]:
                z -= 1
            else:
                mwis.append(z)
                z -= 2
        if z == 1:
            mwis.append(1)
        return mwis
