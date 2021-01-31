class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def addChild(self,data):
        if self.data==data:
            return
        if self.data>data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left=BinaryTree(data)
        if self.data<data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right=BinaryTree(data)
    
    def inOrderTraversal(self):
        elements=[]
        if self.left:#Visit Left Tree 
            elements+=self.left.inOrderTraversal()
        elements.append(self.data)#Base Node
        if self.right:#Right subTree
            elements+=self.right.inOrderTraversal()
        
        return elements
    def preOrderTraversal(self):
        elements=[]
        elements.append(self.data)#Base Node
        if self.left:#Visit Left Tree 
            elements+=self.left.preOrderTraversal()
        if self.right:#Right subTree
            elements+=self.right.preOrderTraversal()
        
        return elements
    def PostOrderTraversal(self):
        elements=[]
        if self.left:#Visit Left Tree 
            elements+=self.left.PostOrderTraversal()
        
        if self.right:#Right subTree
            elements+=self.right.PostOrderTraversal()
        elements.append(self.data)#Base Node
        return elements
    def addValues(self):
        
        leftSum=self.left.addValues() if self.left else 0
            
        rightSum=self.right.addValues() if self.right!=None else 0
           
        add=self.data+leftSum+rightSum
        return add
    def deleteValue(self,value):
        if self.right!=None:
            right=self.right. min()
            return right

    def search(self,value):
        if self.data==value:
            return True
        if self.data>value:
            if self.right:
               return self.right.search(value)
                    
            else:
                return False
        if self.data<value:
            if self.left:
               return self.left.search(value)
            else:
                return False
    def min(self):
        if self.left:
            return self.left.min()
        return self.data
    def max(self):
        if self.right==None:
            return self.data
        if self.right!=None:
            return self.right.max()
    #Delete the node
            
def someFuckingFunction(elements):
    root=BinaryTree(elements[0])
    for i in range(1,len(elements)):
        root.addChild(elements[i])
    root.search(99)
    return root
if __name__=="__main__":
    numbers=[17,4,23,1,20,9,18,34]
    tree=someFuckingFunction(numbers)

    print(tree.inOrderTraversal())
   
    tree.search(9)
    tree.min()
    tree.max()
    print(tree.deleteValue(99))

