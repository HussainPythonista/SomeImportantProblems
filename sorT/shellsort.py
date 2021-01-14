def shellsort(a):
    gap=len(a)//2
    while gap>0:
        for index in range(gap,len(a)):
            currentValue=a[index]
            position=index-gap
            while position+gap>=gap and currentValue<a[position]:
                a[position+gap]=a[position]
                position-=gap
            a[position+gap]=currentValue
        gap=gap//2
    return a
a=[34,2,1,31,3,6,4,7,5,3,1]
print(shellsort(a))