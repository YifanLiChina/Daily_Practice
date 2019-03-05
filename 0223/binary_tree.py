# credit: www.tutorialspoint.com/python/python_binary_tree.htm
class Node:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None

    def insertNode(self, value):
        if self.value:
            if self.left is None:
                self.left = Node(value)
            elif self.right is None:
                self.right = Node(value)
            else:
                print('this node is full')

    def deleteNode(self, value):
        if self.value:
            if value == self.left.value:
                self.left = None
            elif value == self.right.value:
                self.right = None
            else:
                print('there is no such node')

    def PrintTree(self):
        print(self.value)
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()

def createTreeWithList(myList):
    root = Node(myList[0])
    for i in range(1,len(myList)):
        if root.left is None:
            root.left = Node(myList[i])
        elif root.right is None:
            root.right = Node(myList[i])
        else:
            root.left = createTreeWithList(myList[i:])


root = Node(1)
# print(type(root))
# root.insertNode(20)
# root.insertNode(21)
# root.left.insertNode(11)
# root.PrintTree()

aList = [1,2,3,4,5,6,7,8,9,10]
aTree = createTreeWithList(aList)
aTree.PrintTree()
