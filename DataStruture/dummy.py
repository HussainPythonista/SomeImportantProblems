import math
from functools import reduce
def countDigit(n):
    count=0
    while n!=0:
        count+=1
        n//=10
    return count
def mostDigits(listValue):
    maximum=0
    for i in listValue:
        value =countDigit(i)
        maximum=max(value,maximum)
    return maximum

def valueIndex(value,index):
    return math.floor(value/pow(10,index)%10)
def flatten(listValue):
    return reduce(lambda x,y:x+y,listValue)
def radixSort(listValue):
    num=mostDigits(listValue)
    for i in range(num):
        bucket=[[] for _ in range(10)]
        for j in listValue:
            value=valueIndex(j,i)
            bucket[value].append(j)
        #print(bucket)
        listValue=flatten(bucket)
    
    print(listValue)
        

valueIndex(7654452,8)
listValue=(885,42,2,4211,999,34343,22,112212)
radixSort(listValue)


