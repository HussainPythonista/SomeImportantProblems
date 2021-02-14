from itertools import groupby
import itertools
def threeSum(nums):
    listValue=[]
    nums=sorted(nums)
    for i in range(len(nums)-2):
        aPointer=i+1
        bPointer=len(nums)-1
        value=nums[i]+nums[aPointer]+nums[bPointer]
        while aPointer<bPointer:
            value=nums[i]+nums[aPointer]+nums[bPointer]
            if value==0:
                listValue.append([nums[i],nums[aPointer],nums[bPointer]])
                aPointer+=1
                bPointer-=1
            if value>0:
                bPointer-=1
            if value<0:
                aPointer+=1
    val=[]
    for element in listValue:
        if element not in val:
            val.append(element)
    listValue=val
    return listValue
print(threeSum([0,0,0]))
