class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class SinglyLinkedList:
    def __init__(self):
        self.head =None
    def push(self,value):
        if self.head is None:
            node=Node(value)
            self.head = node
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            node=Node(value)
            itr.next=node
    def pop(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            itr=self.head
            while itr.next.next is not None:
                itr=itr.next
            itr.next=None
    def Print(self):
        itr=self.head
        Value=""
        while itr:
            Value+=str(itr.value)+"--->"
            itr=itr.next
        print(Value)
    def pushBegin(self,value):
        node=Node(value)
        node.next=self.head
        self.head=node
ll=SinglyLinkedList()
ll.pushBegin(99)
ll.pushBegin(98)
ll.Print()

