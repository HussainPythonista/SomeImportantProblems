#binarySearchTree
class Node:
    def __init__(self,value) :
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:
    
    def __init__(self):
        self.root=None
    def addValue(self,value):
        node=Node(value)
        if self.root==None:
            self.root=node
            return self.root
        else:
            itr=self.root
            while itr:
                if value<itr.value:
                    if itr.left==None:
                        itr.left=Node(value)
                    else:
                        itr=itr.left#For repeat the same step
                elif value>itr.value:
                    if itr.right==None:
                        itr.right=Node(value)
                    else:
                        itr=itr.right#For repeat the same Step
                    
    def printValue(self):
        pass

tree=BinarySearchTree()
tree.addValue(30)
tree.addValue(20)
tree.addValue(15)
tree.addValue(50)


