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
        if self.root==None:
            self.root=Node(value)
        if self.root!=None:
            current=self.root
            if current.value>value:
                current=current.left
                if current==None:
                    node=Node(value)
                    current=node
                else:
                    self.addValue(value)
            if current.value<value:
                current=current.right
                if current==None:
                    current=Node(value)
                else:
                    self.addValue(value)
            print(current.value)    
    def printValue(self):
        curret=self.root
        elements=[]
        data=[]
        i=0
        while i<range(len(data)):
            curret=data.pop()
            data.append(curret)
            if curret.left:
                data.append(curret.left)
        
        return 
    def buildTree(self,elements):
        root=BinarySearchTree(Node(elements[0]))
        for i in range(1,len(elements)):
            root.addValue(elements[i])
        return root


tree=BinarySearchTree()
tree.addValue(30)
tree.addValue(20)
tree.addValue(15)
tree.addValue(50)
tree.addValue(45)
print(tree.printValue())


