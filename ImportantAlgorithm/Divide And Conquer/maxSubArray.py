def NaiveApproach(array):#this is Big O (n)**2
    maxValue=-999999999999999999999999999999999999999999999999
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            array[i]+=array[j]
            maxValue=max(maxValue,array[i])
    return maxValue
array=[-19,1,2,70,3,-4,10]

def LinearTiming(array):#This Is Kadane's Algorithm
    currentSum=-99999999999999999999999999999999999999999999
    maxValue=currentSum
    for i in range(len(array)):
        currentSum=max(array[i],array[i]+currentSum)
        maxValue=max(maxValue,currentSum)
    return maxValue
def anothemethod(array):
    currentSum=array[len(array)-1]
    maxValue=currentSum
    for i in range(len(array)-2,0,-1):
        currentSum=max(array[i],array[i]+currentSum)
        print(currentSum)
        maxValue=max(currentSum,maxValue)
        
    return maxValue