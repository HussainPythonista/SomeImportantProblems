from ast import walk


def containerWithMostVAlue(array):
    aPointer=0
    bPointer=len(array)-1
    maxValue=0
 
    for i in range(len(array)):
        minValue=array[i]
        for j in range(i,len(array)):
            minValue=min(array[i],array[j])
            maxValue=max(maxValue,minValue*(j-i))
        print(maxValue)
    print(maxValue)    
array=[3,9,3,4,7,2,12,6]
def containerBigOn(array):
    aPointer=0
    bPointer=len(array)-1
    maxValue=0
    while bPointer>aPointer:
        minValue=min(array[aPointer],array[bPointer])
        maxValue=max(maxValue,minValue*(bPointer-aPointer))
        if array[aPointer]<array[bPointer]:
            aPointer+=1
        if array[aPointer]>array[bPointer]:
            bPointer-=1
    print(maxValue)
containerBigOn(array)
