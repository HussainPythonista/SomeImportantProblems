def mergeSort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left=list1[:mid]
        right=list1[mid:]
        mergeSort(left)
        mergeSort(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                list1[k]=left[i]
                print( f"The value which is compare {left[i],right[j]}")
                i+=1
                print(f"i is added=",i)
                k+=1  
            else:
                list1[k]=right[j]
                print( f"The value which is compare {left[i],right[j]}")
                j+=1
                
                print("j is added=",j)
                k+=1  
        while i<len(left):
            list1[k]=left[i]
            i+=1
            
            print("i is added=",i)
            k+=1  
        while j<len(right):
            list1[k]=right[j]
            
            j+=1
            
            print("j is added=",j)
            k+=1  
        
        return list1
print(mergeSort([2,3,4,8,2,1,4,6,8,7,5]))