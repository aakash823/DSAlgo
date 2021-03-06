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


    def lowestcommonnode(self,root,val1,val2):
        if root is None:
            return
        if root.data == val1 or root.data == val2:
            return root
        lefttree = self.lowestcommonnode(root.left,val1,val2)
        righttree = self.lowestcommonnode(root.right,val1,val2)

        if lefttree and righttree:
            return root
        if lefttree is None and righttree is None:
            return None
        return lefttree if lefttree is not None else righttree

    def distancebw2nodes(self,root,val1,val2):
        commonnode = self.lowestcommonnode(root,val1,val2)
        queue = []
        d1,level = 0,0
        queue.append(commonnode)
        while len(queue):
            current = queue.pop(0)
            if current.data == val1:
                d1 +=level
                break
            level+=1
            
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        d2,level = 0 , 0
        queue.append(commonnode)
        while len(queue):
            current = queue.pop(0)
            if current.data == val2:
                d2 +=level
                break
            level+=1
            
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return d1+d2

    def inverttree(self,root):
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.inverttree(root.left)
        self.inverttree(root.right)


    def branchsums(self,root,currentsum,array):
        if root is None:
            return 
        newsums = currentsum + root.data
        if root.left is None and root.right is None:
            array.append(newsums)
        self.branchsums(root.left,newsums,array)
        self.branchsums(root.right,newsums,array)
    #           1
    #         /   \
    #        2     3
    #       / \   /  \
    #      4   5 6    7
    #     /\    \      \
    #    9  11   20      25
    #   /
    #  17
BT = BinaryTree(1)
BT.root.left = Node(2)
BT.root.right = Node(3)
BT.root.left.left = Node(4)
BT.root.left.right = Node(5)
BT.root.right.left = Node(6)
BT.root.right.right = Node(7)
BT.root.left.left.left = Node(9)
BT.root.left.left.right = Node(11)
BT.root.left.right.right = Node(20)
BT.root.right.right.right = Node(25)



inordertravesal = BT.printdata(BT.root,[])
print(inordertravesal)
levelordertraversal = BT.levelorder(BT.root,[])
print(levelordertraversal)
print(BT.lowestcommonnode(BT.root,6,25).data)

array = []
BT.branchsums(BT.root,0,array)
print(array)

BT.inverttree(BT.root)
print(BT.levelorder(BT.root,[]))