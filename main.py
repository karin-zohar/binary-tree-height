class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




def getHeight(root, height=1):
    if (not root.left and not root.right):
        return height
    left_height = getHeight(root.left, height + 1) if root.left else height
    right_height = getHeight(root.right, height + 1) if root.right else height
    return max(left_height, right_height)


def testGetHeight():
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(10)
    root.left.left.left = Node(10)
    root.right = Node(6)
    print('Expected height: 4')
    print('Output height:', getHeight(root))

testGetHeight()