class Node:
    def __init__(self,value,next=None):
        self.prev=None
        self.val=value
        self.next=next
class mergeList:
    def __init__(self):
        self.head=None
    def addValue(self,value):
        if self.head==None:
            node=Node(value)
            self.head=node
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            node=Node(value)
            itr.next=node
            node.prev=itr
    def sortedList(self,a,b):
        result=None
        if a==None:
            return b
        if b==None:
            return a
        if a.val<=b.val:
            result=a
            result.next=self.sortedList(a.next,b)
        else:
            result=b
            result.next=self.sortedList(a,b.next)
        return result
    def mergeSort(self,head):
        #self.printValue()
        if head==None or head.next==None:
            return head
        middle=self.midValue(head)
        nextMid=middle.next
        middle.next=None
        left=self.mergeSort(head)
        right=self.mergeSort(nextMid)
        sortedList=self.sortedList(left,right)
        print(left.val)
        return sortedList
    def midValue(self,head):
        fastMove=head
        slowMove=head
        while fastMove.next!=None and fastMove.next.next!=None:
            slowMove=slowMove.next
            fastMove=fastMove.next.next
        return slowMove
    
    def getLastElement(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        return itr
    def printBackWord(self):
        last=self.getLastElement()
        pass
        while last:
            lasVal+=str(last.val)+"<-"
            last=last.prev
        print(lasVal)
    def printValue(self):
        itr=self.head
        strValue=""
        while itr:
            strValue+=str(itr.val)+"-->"
            itr=itr.next
        print(strValue)

mm=mergeList()
mm.addValue(64)
mm.addValue(3)
mm.addValue(76)
mm.addValue(87)
mm.addValue(53)


print(mm.mergeSort(mm.head))
mm.printValue()
        