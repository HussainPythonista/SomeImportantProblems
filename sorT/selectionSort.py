def selectionSort(a):
    for i in range(len(a)):
        minValue=0
        for j in range(len(a)):
            if a[minValue]<a[j]:
                minValue=j
            a[minValue],a[j]=a[j],a[minValue]
    print(a)
a=[4,3,2,1,14,15,3,2,18]
selectionSort(a)