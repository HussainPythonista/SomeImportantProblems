#SlidingWindow With Deque
#FInd Maximum Value of given K number Of index
array=[1,2,3,1,4,5,2,3,6]
key=3
def bruteForceApproach(array,key):#BigO of n*m
    maxValue=0
    value=maxValue
    for i in range(len(array)-key+1):
        for j in range(key):
            maxValue=max(maxValue,array[i+j])
        print(maxValue,end=" ")


def SlidingWindowAproach(array,k):
    for i in range(len(array)-k+1):
        maxValue=max(array[i:i+k])
        print(maxValue,end=" ")
SlidingWindowAproach(array,key)


