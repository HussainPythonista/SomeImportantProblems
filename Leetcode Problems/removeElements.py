def removeElement(nums, val):
    aPointer=0
    val=0
    for i in range(1,len(nums)-1):
        if nums[aPointer]!=nums[i]:
            aPointer+=1
            nums[aPointer]=nums[i]
            
            print(nums)
    return aPointer
        
nums = [0,0,1,1,1,2,2,3,3,4,4,4,4,5]
val = 3
print(removeElement(nums,val))