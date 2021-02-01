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
        if self.left!=None:
            return self.left.min()
        else:
            return self.data
    def max(self):
        if self.right==None:
            return self.data
        if self.right!=None:
            return self.right.max()
    #Delete the node
    def delete(self,value):
        if value<self.data:
            if self.left!=None: #For checking the left side is Not None
                self.left=self.left.delete(value)
        elif value>self.data:#For checking the rightt side is Not None
            if self.right!=None:
                self.right=self.right.delete(value)
        else:

            if self.right==None and self.left==None:#Reaching Last Node
                return None
            if self.left==None:#If left node has None but right has only one node
                return self.right
            if self.right==None:#If right node has None but leftt has only one node
                return self.left

    #For the Node With two Child
            #minValue=self.right.min()
            #self.data=minValue
            #self.right=self.right.delete(minValue)

            maxValue=self.left.max()
            self.data=maxValue
            self.left=self.left.delete(self.data)
        return self
    def level(self):
        i=0
        while self.left:
            if self.left==None:
                break
            else:
                i+=1
        return i

            
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
   
    tree.search(4)
    tree.min()
    tree.max()
    tree.delete(1)
    print(tree.level())
    print(tree.inOrderTraversal())
    

