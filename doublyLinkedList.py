#Doubly linked list contains two References
#prevReference
#nextReference
class Node:
    def __init__(self,value,prev=None,next=None):
        self.value = value
        self.prev = prev
        self.next = next
class doublyLinkedList:
    def __init__(self,head=None):
        self.head = head
    def inserBegin(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            node=Node(value)
            node.next=self.head
            node.prev=None
            self.head.prev=node      
            self.head=node
    def getLast(self):
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        return itr
    def printReverse(self):
        
            last=self.getLast()
            itr=last
            string=""
            while itr is not None:
                string+=str(itr.value)+"<----"
                itr=itr.prev
            print(string)
    def insertByDataAfter(self, data,value):
        if self.head is None:
            return
        else:
            itr=self.head
            while itr:
                if itr.value==data:
                    node=Node(value)
                    node.next=itr.next
                    node.prev=itr
                    itr.next.prev=node
                    if itr.next==None:
                        itr.next.prev=node
                    itr.next=node
                    break
                itr=itr.next
    def deleteBegin(self):
        self.head=self.head.next
        self.head.prev=None
    def deleteLast(self):
        itr=self.head
        while itr.next.next is not None:
            itr=itr.next
        itr.next=None
    def insertBefore(self,data,value):
        itr=self.head
        while itr.next:
            if itr.next.value==data:
                node=Node(value)
                node.next=itr
                node.prev=itr.prev
                itr.next.prev=node
                itr.next=node
                break
            itr=itr.next
    def deleteAfter(self,data):
        itr=self.head
        while itr.next:
            if itr.value==data:
                itr.next.prev=itr.prev
                itr.prev.next=itr.next
                break   
            itr=itr.next    

    def insertLast(self,value):
        if self.head is None:
            node=Node(value)
            self.head=node
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            node=Node(value)
            itr.next=node
            node.prev=itr
            itr=node

    def insertValue(self,listValue):
        for i in listValue:
            self.insertLast(i)
    def printValue(self):
        itr=self.head
        string=""
        while itr:
            string+=str(itr.value)+"--->"
            itr=itr.next
        print(string)
    
ll=doublyLinkedList()
listValue=["Apple","Banana","Orange","JackFruit","Graphs"]
ll.insertValue(listValue)
ll.printReverse()
ll.printValue()