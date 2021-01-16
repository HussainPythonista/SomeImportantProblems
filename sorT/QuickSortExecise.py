def swap(listValue,a,b):
    if a!=b:
        listValue[a],listValue[b]=listValue[b],listValue[a]
def partition(listValue,start,end):
    pivotIndex=len(listValue)-1
    pivot=listValue[end]
    
    pIndex=start
    
    for i in range(start,end):
            if listValue[i]<=pivot:
                swap(listValue,pIndex,i)
                pIndex+=1
    swap(listValue,pIndex,end)    
        
    return pIndex

def quicksort(listValue,start,end):
    if len(listValue)==1:
        return
    if start<end:
        pi=partition(listValue,start,end)
        quicksort(listValue,pi+1,end)
        quicksort(listValue,start,pi-1)
    return listValue
listValue=[11,9,29,7,2,15,28]
print(quicksort(listValue,0,len(listValue)-1))
