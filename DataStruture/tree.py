class treeNode:
    def __init__(self,data=None):
        self.parents=None
        self.data=data
        self.children=[]
    def getLevel(self):
        i=0
        current=self.parents
        
        while current:
            i+=1
            current=current.parents
        return i
    def addChild(self,child):
        child.parents=self
        self.children.append(child)
    
    def printDatas(self):
        spaces=" "*self.getLevel()*2
        if len(spaces)>0:
            prefix=spaces+"|__"
        else:
            prefix=""

        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.printDatas()
        
def treeDataStructure():
    root=treeNode("Electronics")

    laptop=treeNode("Laptop")
    laptop.addChild(treeNode("Lenovo"))
    laptop.addChild(treeNode("MacBook"))
    laptop.addChild(treeNode("MicroSoft Surface"))

    mobiles=treeNode("Mobiles")
    mobiles.addChild(treeNode("OnePlus"))
    mobiles.addChild(treeNode("Iphone"))
    mobiles.addChild(treeNode("Mi"))
    condoms=treeNode(("Condoms"))
    
    condoms.addChild(treeNode("Manforce"))
    condoms.addChild(treeNode("Moods"))
    condoms.addChild(treeNode("Durex"))
    
    root.addChild(laptop)
    root.addChild(mobiles)
    root.addChild(condoms)
    mobiles.getLevel()
    return root
    
root=treeDataStructure()
root.printDatas()
