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
    def breadthFirstSearch(self):  
        #Create deque
        node=self.root
        data=[]
        queue=[]
        queue.append(node)
        while len(queue)>0:
            node=queue.pop(0)
            #data+=str(node.value)+"->"
            data.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return data
    def preOrderTraversal(self):
        node=self.root
        data=[]
        stack=[]
        stack.append(node)
        while len(stack)>0:
            node=stack.pop()
            data.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    def inOrderTraversal(self):
        node=self.root
        stack=[]
        data=[]
        while True:
            if node:
                stack.append(node)
                node=node.left
            elif stack:
                node=stack.pop()
                data.append(node.value)
                node=node.right
            else:
                break
        return data        
def BuildTree(elements):
        root=BinarySearchTree()
        root.addValue(elements[0])
        for i in range(1,len(elements)):
            root.addValue(elements[i])
        
        return root
numbres=[4,3,1]
root=BinarySearchTree()
root.addValue(10)

root.addValue(15)
root.addValue(6)

root.addValue(3)
root.addValue(8)
root.addValue(20)

root=root.inOrderTraversal()
print(root)









