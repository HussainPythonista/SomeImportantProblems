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
            
    def sortVal(self):
        newList=[]
        itr=self.head
        while itr.next:
            newList.append(itr.val)
            itr=itr.next
        newList=sorted(newList,key=lambda node:node)
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

mm.addValue(99)
mm.addValue(76)
mm.addValue(92)
mm.addValue(53)
mm.addValue(64)
mm.addValue(3)
mm.sortVal()
mm.printValue()
        