class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

#node=Node(19)
#node.next=Node(39)
#node.next.next=Node(600)
#node.next.next.next=Node(6431)
#print(node.next.value)
class SinglyLinkedList:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
    def getLength(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        return count
    def lastValue(self):
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        return itr
    def push(self,value):
        if self.head is None:
            node=Node(value)
            self.head = node
            self.tail = node
        else:
            current=self.head
            newTail=current
            while current.next is not None:
                newTail=current
                current=current.next
            current.next=Node(value)
            newTail=current.next
            self.tail=newTail
        
    def print(self):
        if self.head is None:
            print("Linked lIst is Empty")
        else:
            itr=self.head
            newTail=itr
            string=""
            while itr:
                string+=str(itr.value)+"--->"
                newTail=itr
                itr=itr.next
            #print(f"The head is {self.head.value} and tail is {self.tail.value}")
            print(string)
            
            
    def insertBegin(self,value):
            node=Node(value)
            node.next=self.head
            self.head=node
            
            newTail=self.lastValue()
            self.tail=newTail
    def pop(self):
        if self.head.next is None:
            self.head=self.tail=None
        else:
            itr=self.head
            newTail=itr
            while itr.next.next is not None:
                itr=itr.next
            itr.next=None
            newTail=itr.next
            self.tail=newTail
    def removeAtBegin(self):
        if self.head is None:
            return
        else:
            
            self.head=self.head.next
    def getValueByIndex(self,index):
        if index>self.getLength():
            return "Index is out of list"
        else:
            itr=self.head
            index=index
            count=0
            while itr.next:
                if count+1==index:
                    return itr.value
                itr=itr.next
                count+=1
    def insertValue(self,listValue):
        for i in listValue:
            self.push(i)
    def changeValue(self,update,value):
        itr=self.head
        while itr:
            if itr.value==value:
                itr.value=update
            itr=itr.next
    def deleteByIndex(self,index):
        if index>self.getLength() or index<0:
            print("Index out of range")
        elif self.head is None:
            print("Linked list is Empty")
            
        else:
            count=0
            itr=self.head
            while itr:
                if index==self.getLength():
                    self.pop()
                if count+1==index:
                    itr.next=itr.next.next
                count+=1
                itr=itr.next
    def reversed(self):
        #Swap the Variable
        #  //A--->B--->C--->D
        current=self.head  #Banana is head
        prev=None#For back reference
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        self.head=prev
        
sll=SinglyLinkedList()
listValue=["Banana","orange","Graphs","Litchie"]
sll.insertValue(listValue)
sll.reversed()
sll.print()