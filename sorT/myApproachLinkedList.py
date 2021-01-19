class Node:#Create the Node
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
#node=Node(11)
#node.value=12
#print(node.value)
#This Contains Only Node
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head#Starting Point of Linked List
        
    def atBegin(self,value):
        node=Node(value)
        node.next=self.head
        self.head = node
    def insertLast(self,value):
        if self.head is None:
            self.head =Node(value)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            node = Node(value)
            itr.next=node
    
    def printValue(self):
        itr=self.head
        string=""
        while itr:
            string+=str(itr.value)+"--->"
            itr=itr.next
        print(string)
    def insertBeforeTheValue(self,before,value):
        
        if self.head is None:
            print("Linked List is Empty")
        else:
            
            itr=self.head
            
            while itr.next:
                if itr.next.value == before:
                        node= Node(value)
                        node.next=itr.next
                        itr.next=node
                        break
                if self.head.value ==before:
                    node=Node(value)
                    node.next=self.head
                    self.head=node    
                itr=itr.next
    def deleteBefore(self,before):
        if self.head is None:
            print("Linked List is Empty")
        else:
            itr=self.head
            while itr.next.next:
                if itr.next.next.value==before:
                    itr.next=itr.next.next
                    break
                itr=itr.next
    def count(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def pop(self):
        if self.head is None:
            print("Linked List is Empty")
        elif self.head.next is None:
            self.head=None
        else:
                itr=self.head
                while itr.next.next is not None:
                    itr=itr.next
                itr.next=None

    def deleteByIndex(self,index):
        if index==self.count():
            pass
        count=0
        itr=self.head
        while itr:
            
            if index-1==count:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
        if index==0:
            self.head=self.head.next
        
    
    def addByIndex(self,index,value):
        if index==0:
            node=Node(value)
            node.next=self.head
            self.head=node

        count=0
        itr=self.head
        while itr:
            if index-1==count:
                node=Node(value)
                node.next=itr.next
                itr.next=node
                break
            itr=itr.next
            count+=1
        
            

                
    def insertAfterTheValue(self,after,value):
        if self.head is None:
            print("linkedList is empty")
        else:
            itr=self.head
            while itr:
                if itr.value==after:
                    node=Node(value)
                    node.next=itr.next
                    itr.next=node
                    
                itr=itr.next    
    def insertValue(self,listValue):
        for i in (listValue):
            self.insertLast(i)
ll=SinglyLinkedList()
listValue=set([1,2,3,4])
ll.insertValue(listValue)
ll.insertBeforeTheValue(1,'kalanthar')


ll.addByIndex(0,"Mohamed")
ll.addByIndex(1,9)
ll.addByIndex(3,9)
ll.deleteByIndex(7)
ll.printValue()
