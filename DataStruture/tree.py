class treeNode:
    def __init__(self,data=None):
        self.parents=None
        self.data=data
        self.children=[]

    def addChild(self,data):
        self.parents=self
        self.children.append(data)
    def printDatas(self):
        if len(self.children)>1:
            for child in self.children:
                print(child.data)
def treeDataStructure():
    root=treeNode("Electronics")
    laptop=treeNode("Laptop")
    laptop.addChild("Lenovo")
    laptop.addChild("MacBook")
    laptop.addChild("MicroSoft Surface")
    mobiles=treeNode("Mobiles")
    mobiles.addChild("OnePlus")
    mobiles.addChild("Iphone")
    mobiles.addChild("Mi")
    condoms=treeNode("Condoms")
    condoms.addChild("Manforce")
    condoms.addChild("Moods")
    condoms.addChild("Durex")
    
    root.addChild(laptop)
    root.addChild(mobiles)
    root.addChild(condoms)
    
treeDataStructure()