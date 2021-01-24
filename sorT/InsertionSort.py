def InsertionSort(listValue):
    #Pointer
    for pointer in range(1,len(listValue)):
        current=listValue[pointer]
        sortedArray=pointer-1
        while sortedArray>=0 and current<listValue[sortedArray]:
            listValue[sortedArray+1]=listValue[sortedArray]
            sortedArray-=1#To check the values inside the sortedArray
       
        listValue[sortedArray+1]=current
    return listValue
listValue=[5,3,2,4,21,4,54,54,321]
print(InsertionSort(listValue))