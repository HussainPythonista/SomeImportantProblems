class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addValue(self,value):
        if self.head is None:
            node=Node(value)
            node.next=self.head
            self.head=node
        else:
            itr=self.head
            while itr.next:
                
                    itr=itr.next
            else:
                    node=Node(value)
                    itr.next=node
    def reverseLinkedList(self):
        prev=None
        current=self.head
        while current:
            newValue=current.next
            current.next=prev
            prev=current
            current=newValue
        self.head=prev
    def printValue(self):
        if self.head is None:
            print("None")
        else:
            itr=self.head
            lisTvalue=[]
            while itr:
                lisTvalue.append(itr.value)
                itr=itr.next
            return lisTvalue

                    
l1=LinkedList()
l1Value=[9,9,9,9,9,9,9]
for value in l1Value:
    l1.addValue(value)

l1Value=l1.printValue()
print(l1Value)


l2=LinkedList()
l2Value=[9,9,9,9]
for value in l2Value:
    l2.addValue(value)
l2Vlaue=l2.printValue()

def addLinkedList(l1Value,l2Value):
    
    value=""
    value2=""
    for i in l1Value:
        value+=str(i)
    for j in l2Value:
        value2+=str(j)
    value3=int(value)+int(value2)
    return (value3)

newValue=(addLinkedList(l1Value,l2Vlaue))
final=LinkedList()
for i in str(newValue):
   final.addValue(int(i))
final.reverseLinkedList()
print(final.printValue())















#LeetCode Solution



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:#It Come from server


        dummYhead=ListNode(0)#For creating Node
        p1=l1
        p2=l2
        current=dummYhead
        carry=0#For Adding 10 as 0 in number 1 in upcomming number
        while p1 or p2 :
           
            val1=p1.val if p1 else 0
            
            val2=p2.val if p2 else 0
            
            carry,out=divmod(val1+val2+carry,10)
            current.next=ListNode(out)
            current=current.next
            p1=p1.next if p1 else None
            p2=p2.next if p2 else None
        if carry>0:
            current.next=ListNode(carry)
        return dummYhead.next
        
