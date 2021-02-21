def maxSubArray(nums):
    if len(nums)>0:
        maxValue=0
        if len(nums)>1:
            aPointer=0
            val=0
            
            bPointer=0

            maxValue=-10000000000000000000
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    val+=nums[j-i]
                    print(val)
                maxValue=max(maxValue,nums[i])
            return maxValue
        else:
            maxValue=nums[0]
            return maxValue
    else:
        return []
                
print(maxSubArray([-2,1]))