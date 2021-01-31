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
        else:
            current=self.root
            while current:
                if value<current.value:
                    if current.left==None:
                        current.left=Node(value)
                        return current.left
                    else:
                        current=current.left
                if value>current.value:
                    if current.right==None:
                        current.right=Node(value)
                        return current.right
                    else:
                        current=current.right
        return self.root
    def searchTheElement(self,element):
        found=False
        current=self.root
        while found==False and current:
            if element<current.value:
                current=current.left
            elif element>current.value:
                current=current.right
            else:
                print("Found")
                found=True
        if found==False:
            return "Not Found"
        return element   
    def inOrderTraverse(self):
        pass
        
def BuildTree(elements):
        root=BinarySearchTree()
        root.addValue(elements[0])
        for i in range(1,len(elements)):
            root.addValue(elements[i])
        
        return root
numbres=[4,3,1]
root=BinarySearchTree()
root.addValue(50)
root.addValue(60)
root.addValue(55)

root.addValue(40)
root.addValue(45)
root.inOrderTraverse()
print(root.root.left.right.value)
print(root.searchTheElement(60))







