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
    
    def printDatas(self,require):
        require=require.lower()
        spaces=" "*self.getLevel()*2
        if len(spaces)>0:
            prefix=spaces+"|__"
        else:
            prefix=""
        if require=="both":
            print(prefix+f"{self.data[0]}"+f" ({self.data[1]})")
        elif require=="name":
            print(prefix+f"{self.data[0]}")
        elif require=="designation":
            print(prefix+f"{self.data[1]}")
        if self.children:
            for child in self.children:
                child.printDatas(require)
        
def treeDataStructure():
    root=treeNode(("Nilupul","CEO"))

    cto=treeNode(("Chinmay","CTO"))
    infraHead= treeNode(("Viswa","InfraStructure Head"))
    infraHead.addChild(treeNode(("Dhaval","Cloud Manager")))
    infraHead.addChild(treeNode(("Abijit","App Manager")))
    appHead=treeNode(("Aamir","Application Head"))
    cto.addChild(infraHead)
    cto.addChild(appHead)
    HR=treeNode(("Gels","HR Head"))
    requireHead=treeNode(("Peter","Requirement Managers"))
    policyMan=treeNode(("Waqas","Policy Manager"))
    HR.addChild(requireHead)
    HR.addChild(policyMan)
    root.addChild(cto)
    root.addChild(HR)

    return root
root=treeDataStructure()
root.printDatas("BOTH")
