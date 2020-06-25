from TreeNode import Node
import heapq


class Huffman:
    def __init__(self, filePath):
        self.nodes, self.weights = self.readFile(filePath)
        self.huff_codes = {}

    def readFile(self, filePath):
        with open(filePath) as fin:
            nodes, weights = {}, []
            for count, line in enumerate(fin.readlines()[1:]):
                weight = int(line)

                # Add new node back into nodes. If the weight is already in nodes, use probing to insert.
                i = 0
                while weight + i in nodes:
                    i += 1
                nodes[weight + i] = Node.Node(str(count))
                heapq.heappush(weights, weight+i)

        return nodes, weights

    def huffman(self):
        root = self.tree(self.nodes, self.weights)
        self.codes(root)
        return root, self.huff_codes

    def tree(self, nodes, weights):
        while len(nodes) != 1:
            weight1 = heapq.heappop(weights)
            weight2 = heapq.heappop(weights)

            child1, child2 = nodes[weight1], nodes[weight2]
            del nodes[weight1]
            del nodes[weight2]

            symbol1, symbol2 = child1.value, child2.value
            joinedSymbol = symbol1 + "+" + symbol2
            root = Node.Node(joinedSymbol, child2, child1)

            # Add new node back into nodes. If the weight is already in nodes, use probing to insert.
            i = 0
            while weight1 + weight2 + i in nodes:
                i += 1
            nodes[weight1 + weight2 + i] = root
            heapq.heappush(weights, weight1 + weight2 + i)

        return next(iter(nodes.values()))

    def codes(self, root, path=''):
        if root.isLeaf():
            self.huff_codes[root.value] = path
        else:
            path_left = path + '0'
            path_right = path + '1'

            self.codes(root.right, path_right)
            self.codes(root.left, path_left)

    def find_MinMax_length(self):
        minimum = float('inf')
        maximum = 0
        for path in self.huff_codes.values():
            maximum = max(maximum, len(path))
            minimum = min(minimum, len(path))
        return maximum, minimum
