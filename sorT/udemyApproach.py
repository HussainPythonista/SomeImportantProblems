class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class SinglyLinkedList:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
    def pushBegin(self,value):
        node=Node(value)
        node.next=self.head
        self.tail=node
        self.head=node
    def printValue(self):
        current=self.head
        string=""
        while current:
            string+=str(current.value)+"---->"
            current=current.next
        print(string)
    def pop(self):
        if self.head.next is  None:
            self.head =None
        else:
            current=self.head
            while current.next.next!=None:
                current=current.next
            current.next=None
       
        
sll=SinglyLinkedList()
sll.pushBegin(66)
sll.pushBegin(66)

sll.printValue()