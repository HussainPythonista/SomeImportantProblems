from typing import Counter


def smallestValue(value,array):
    windowStart=0
    currentWindow=0
    minValue=10000000000
    count=0
    for windowEnd in range(len(array)):
        currentWindow+=array[windowEnd]
        while currentWindow>=value:
            minValue=min(minValue,windowEnd-windowStart+1)
            currentWindow-=array[windowStart]
            windowStart+=1
    return minValue
array2=[4,2,2,7,1,2,3,1,3,49]
value=8
print(smallestValue(value,array2))