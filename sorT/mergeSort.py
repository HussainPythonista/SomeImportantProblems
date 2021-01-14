def mergeSort(arraylist,key,decending):
    if len(arraylist)<=1:
        return arraylist
    else:
        mid=len(arraylist)//2
        leftSide=arraylist[:mid]
        rightSide=arraylist[mid:]
        mergeSort(leftSide,key,decending)
        mergeSort(rightSide,key,decending)
    return conqure(leftSide,rightSide,arraylist,key,decending)
def conqure(leftSide,rightSide,arraylist,key,decending):
        i=j=k=0
        while i<len(leftSide) and j<len(rightSide):
            if decending ==False:
                if leftSide[i][key]<rightSide[j][key]:
                    arraylist[k]=leftSide[i]
                    i+=1
                    k+=1
                else:
                    arraylist[k]=rightSide[j]
                    j+=1
                    k+=1
            else:
                if leftSide[i][key]>rightSide[j][key]:
                    arraylist[k]=leftSide[i]
                    i+=1
                    k+=1
                else:
                    arraylist[k]=rightSide[j]
                    j+=1
                    k+=1
        while i<len(leftSide):
            arraylist[k]=leftSide[i]
            i+=1
            k+=1
        while j <len(rightSide):
                arraylist[k]=rightSide[j]
                j+=1
                k+=1
        return arraylist
key="name"
elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
for i in elements:
    print(i)
print(mergeSort(elements,key,decending=True))
    