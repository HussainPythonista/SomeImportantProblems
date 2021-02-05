#Problem 1
def sumKDistictNumber(array,k):#Big O of N
    maxValue=0
    for i in range(len(array)-k+1):
        firstMax=sum(array[i:i+k])
        print(firstMax)
        maxValue=max(maxValue,firstMax)
    print(maxValue)
array1=[1,3,4,2,6,3]
k=3
#Method 2
def sumKDistictNumber2(array1,k):#BiG O n
    maxValue=0
    window=0
    for i in range(k):
        maxValue+=array1[i]
    window=maxValue
    for j in range(k,len(array1)):
        temp=window-array1[j-k]
        window=temp+array1[j]
        maxValue=max(window,maxValue)
    return maxValue
array1=[1,3,4,2,6,3]
k=3
print(sumKDistictNumber2(array1,k))
#Brute Force Approach
def bruteFOrce(array,k):#Big O (n*m)
    maxValue=0
    for i in range(len(array)-k+1):
        Value=0
        for j in range(i,i+k):
            Value+=array[j]
        maxValue=max(maxValue, Value)
    return maxValue

            
