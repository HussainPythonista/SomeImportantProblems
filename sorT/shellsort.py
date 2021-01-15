def shellSort(listValue):
    gap=len(listValue)//2
    while gap>0:
        for i in range(gap,len(listValue)):
            currentValue=listValue[i]
            position=i-gap
            while position+gap>=gap and listValue[position]>currentValue:
                listValue[position+gap]=listValue[position]
                position-=gap
            listValue[position+gap]=currentValue
        gap=gap//2
    return listValue
listValue=[4,2,2,3,3,2,4,4,22,4,5,56,99,2,2,]
print(shellSort(listValue))