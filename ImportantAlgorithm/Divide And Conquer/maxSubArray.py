def naiveApproach(listValue):
    maxValue=0
    for i in range(len(listValue)):
        for j in range(i+1,len(listValue)):
            listValue[i]+=listValue[j]
            maxValue=max(listValue[i],maxValue)
    print(maxValue)

def maxSubArray(listValue):#Optimal Solution O(n)
    maxValue=0
    current=0
    for i in range(1,len(listValue)):
        current=max(listValue[i],current+listValue[i])
        maxValue=max(current,maxValue)

    return maxValue
listValue=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(listValue))
