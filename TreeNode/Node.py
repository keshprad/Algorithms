

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        if left is None or isinstance(left, Node):
            self.left = left
        else:
            raise NodeTypeError('left child must be a Node instance')

        if right is None or isinstance(right, Node):
            self.right = right
        else:
            raise NodeTypeError('right child must be a Node instance')

    def isLeaf(self):
        return self.left is None and self.right is None