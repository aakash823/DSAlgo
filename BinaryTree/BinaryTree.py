class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,data):
        self.root = Node(data)

    def printdata(self,root,array):
        if root is not None:
            self.printdata(root.left,array)
            array.append(root.data)
            self.printdata(root.right,array)
        return array

    def levelorder(self,root,array):
        if root is None:
            return 
        queue = []
        queue.append(root)
        while len(queue):
            current = queue.pop(0)
            array.append(current.data)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return array
        #1
    #   / \
    #  2   3
    # / \ /  \
    #4  5 6   7
BT = BinaryTree(1)
BT.root.left = Node(2)
BT.root.right = Node(3)
BT.root.left.left = Node(4)
BT.root.left.right = Node(5)
BT.root.right.left = Node(6)
BT.root.right.right = Node(7)
inordertravesal = BT.printdata(BT.root,[])
print(inordertravesal)
levelordertraversal = BT.levelorder(BT.root,[])
print(levelordertraversal)