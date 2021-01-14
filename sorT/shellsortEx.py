
def duplicates(a):
    duplicates={}
    for i in range(len(a)):
        if a[i] in duplicates:
            duplicates[a[i]]=1
        else:
            duplicates[a[i]]=1
    newListValue=duplicates.keys()
    return shellsort(newListValue)
def shellsort(list1):
    gap=len(list1)//2
    while gap>0:
        for index in range(gap,len(list1)):
            current=list1[index]
            position=index-gap
            while gap<=(position+gap) and current<list1[position]:
                list1[position+gap]=list1[position]
                position-=gap
            list1[position+gap]=current
        gap=gap//2
    return list1
a=[3,2,1,3,3,2,3,1,1,99,43,2,1]
print(duplicates(a))