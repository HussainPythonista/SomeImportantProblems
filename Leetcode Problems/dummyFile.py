def TwoSumMyApproach(array,target):
    value=0
    for j in range(len(array)):
        value=array[j]+array[j+1]
        
        if value==target:
            return [j,j+1]
        print(value)

        
        
target=9
array=[1,11,7,2]
print(TwoSumMyApproach(array,target))