def removeDuplicates(nums):
    aPointer=0
    val=0
    bPointer=0
    for pointer in range(1,len(nums)):
        if nums[aPointer]!=nums[pointer]:
            aPointer+=1
            nums[aPointer]=nums[pointer]
    return aPointer+1
            
array=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(array))