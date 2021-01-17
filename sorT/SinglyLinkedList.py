class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class SinglyLinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
    def push(self,value):
        if self.head is None:
            node=Node(value)
            self.head = node
            self.tail = node
        else:
            #nextRef=self.head
            #while nextRef.next is not None:
            #    nextRef=nextRef.next
            #nextRef.next=Node(value)
            #self.tail=nextRef
            node=Node(value)
            self.tail.next=node
            self.tail=node
    def pop(self):
        

        if self.head is None:
            print("Linked List is empty")
        else:
            itr=self.head
            newTail=itr
            while itr.next:
                newTail=itr
                itr=itr.next
                
            self.next=newTail
            newTail.next=None
        if self.head ==self.tail:
            self.head=self.tail=None
    def pushBegin(self,value):
            node=Node(value)
            node.next=self.head
            node.tail=None
            self.head=node
    def Print(self):
        itr=self.head
        Value=""
        while itr:
            Value+=str(itr.value)+"--->"
            itr=itr.next
        print(Value)
ll=SinglyLinkedList()
ll.pushBegin(99)
ll.pushBegin(745)
ll.pushBegin(99)

ll.Print()

