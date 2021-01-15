def swap(a,b,listValue):
    if a!=b:
        listValue[a],listValue[b]=listValue[b],listValue[a]
    return listValue
def partition(start,end,a):
    pivotIndex=start
    pivot=a[start]
    start=pivotIndex+1
    end=len(a)-1
    while start<end:
        while start<len(a) and a[start]<=pivot:
            start+=1
        while a[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,a)
        else:
            swap(pivotIndex,end,a)
    return end
def quickSort(start,end,listValue):
    if start<end:
        pi=partition(start,end,listValue)
        quickSort(start,pi-1,listValue)
        quickSort(pi+1,end,listValue)
    return listValue
a=[11,9,29,7,2,15,28]
print(quickSort(0,len(a)-1,a))