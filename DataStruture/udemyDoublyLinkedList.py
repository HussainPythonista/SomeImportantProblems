class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        self.prev=None
class DoublyLinkedList:
    def __init__(self,head=None):
        self.head = head
    def printForward(self):
        if self.head is None:
            print("Linked lIst is Empty")
        else:
            string=""
            itr=self.head
            while itr:
                string+=str(itr.value)+"--->"
                itr=itr.next
            print(string)
    def push(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
        else:
            itr=self.head
            while itr.next is not None:
                itr=itr.next
            
            itr.next=node
            node.next=None
            node.prev=itr
    def lastNode(self):
        itr=self.head
        while itr.next is not None:
            itr=itr.next
        return itr
    def printReverse(self):
        last=self.lastNode()
        itr=last
        string=""
        while itr:
            string+=str(itr.value)+"<---"
            itr=itr.prev
        print(string)
    def PushBegin(self,value):
        
        node=Node(value)
        node.next=self.head
        node.prev=None
        self.head.prev=node
        self.head=node
    def pop(self):
        if self.head is None:
            print("Linked List is Empty")
        if self.head.next is None:
            self.head =None
        else:
            itr=self.head
            while itr.next.next is not None:
                itr = itr.next
            itr.next=None

    def deleteByValue(self,value):
        pass
ll=DoublyLinkedList()
ll.push(99)
ll.push(76)
ll.PushBegin("First Value")
ll.pop()
ll.printReverse()
ll.printForward()