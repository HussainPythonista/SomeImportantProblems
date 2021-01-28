def median(listValue):
    mid=len(listValue)//2
    if len(listValue)%2==1:
        return listValue[mid]
    else:
        left=listValue[mid-1]
        right=listValue[mid]
        return float((left+right)/2)

    
list1=[1,2]
list2=[3,4]
newList=list1+list2
newList=sorted(newList)
print(newList)
print(median(newList))