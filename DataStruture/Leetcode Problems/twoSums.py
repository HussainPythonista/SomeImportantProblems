#Approach 1
def twoSum(target,listValue):
    i=0
    for _ in range(len(listValue)):
        for outer in range(1,len(listValue)):
            for inner in range(outer):
                if listValue[inner]+listValue[outer]==target:
                    return [outer,inner]
        
target=0
listValue=[-3,4,3,90]
twoSum(target,listValue)
#approach 2
def twoSum(target,listValue):
    start=0
    end=len(listValue)-1
    for i in range(len(listValue)):
        if listValue[start]+listValue[end]<target:
            start+=1
        if listValue[start]+listValue[end]>target:
            end-=1
        else:
            return [start,end]

target=6
listValue=[3,2,4]
#Approach 3




def twoSum1(target,listValue):
    dictValue={}
    for i in range(len(listValue)):
        secondTarget=target-listValue[i]
        if secondTarget in dictValue:
            return [dictValue[secondTarget],i]
        dictValue[listValue[i]]=i    
target=6
listValue=[3,2,4]
print(twoSum1(target,listValue))