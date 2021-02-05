#NaiveApproach
import math
def NaiveApproachh(a, b):
    maxValue=0
    i=0
    while i<len(a)-b+1:
        for j in range(b):
            print(a[i]+a[i+j])
        i+=1


#Sliding Window Aproach
def slidingWindow(array,Value):
    #This one is fixed Length
    maxValue=0
    window=0
    
    for i in range(Value):
        maxValue+=array[i]
    window=maxValue
    for slide in range(Value,len(array)):
        temp=window-array[slide-Value]#FOr Shrinking the Value
        window=temp+array[slide]
        maxValue=max(maxValue,window)

    return maxValue
a=[7,5,2,11,0,2,8,12,13]
b=3

def contineousLongestString(array):
    maximum=0
    #count=0
    for i in range(len(array)-1):
        anchor=i
        if array[i]<array[i+1]:
            #count+=1
            #print(count)
            maximum=max(maximum,anchor)
    return maximum#count)

array=[1,2,3,5,4,7]

def smallestValue(value,array):
    windowStart=0
    currentWindow=0
    minValue=10000000000
    for windowEnd in range(len(array)):
        currentWindow+=array[windowEnd]
        while currentWindow>=value:
            #print(windowEnd-windowStart)
            minValue=min(minValue,windowEnd-windowStart+1)
            currentWindow-=array[windowStart]
            windowStart+=1 
    print(minValue)
array2=[4,2,2,10,1,2,3,1,3,49]
value=8
smallestValue(array=array2,value=value)
def contigeousSum(arraY,key):
    sumValue=sum(arraY[:key])
    for i in range(len(arraY)-key+1):
        sumValue=max(sumValue,sum(arraY[i:i+key]))
    print(sumValue)



def LongestSubString(array,k):
    dictValue={}
    value=0
    for i in range(len(array)):
        if len(dictValue)<k:
            if array[i] in dictValue:
                dictValue[array[i]]+=1
            else:
                dictValue[array[i]]=1
        pass

    
    print(dictValue)
array4=["A","A",'A',"H","H","I","B","C"]
LongestSubString(array4,3)
