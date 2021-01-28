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
    
    def printDatas(self,level):
        if level>=self.getLevel():
            spaces=" "*self.getLevel()*2
            if len(spaces)>0:
                prefix=spaces+"|_ _"
            else:
                prefix=""

            print(prefix+self.data)
            if self.children:
                for child in self.children:
                    child.printDatas(level)
                    
def treeDataStructure():
    globals=treeNode("Global")
    india=treeNode("India")
    
    gujarat=treeNode("Gujarat")
    gujarat.addChild(treeNode("Surat"))
    gujarat.addChild(treeNode("Baroda"))
    gujarat.addChild(treeNode("Ahmadabad"))
    karnataka=treeNode("Karnataka")
    karnataka.addChild(treeNode("Bangalore"))
    karnataka.addChild(treeNode("Mangalore"))
    karnataka.addChild(treeNode("Kudagu"))
    india.addChild(gujarat)
    india.addChild(karnataka)
    usa=treeNode("USA")
    newJersey=treeNode("New Jersey")

    california=treeNode("California")
    california.addChild(treeNode("San Fransisco"))
    california.addChild(treeNode("Mountain view"))
    california.addChild(treeNode("Palo Alto"))

    newJersey.addChild(treeNode("Prinston"))
    newJersey.addChild(treeNode("Trenton"))

    usa.addChild(california)
    usa.addChild(newJersey)
    globals.addChild(india)
    globals.addChild(usa)
    return globals
    
root=treeDataStructure()
root.printDatas(3)