#The Time Complexity for RadixSort is bigO of 
import math
def ValueOfIndex(num,i):#To know the value in integer by index
    strNum=str(num)
    reverseOfstrNum=strNum[::-1]
    if i>len(reverseOfstrNum):
        return 0
    else:
        return reverseOfstrNum[i]
ValueOfIndex(6543,2)
    #or
def ValueOfIndex2(num,i):
    #The math.floor give us to whole value ex.9.654 by 9
    #abs is used for -1 as 1
    #pow(10,i)--->10 is used for calculate digit 
    # ex i=2 10**2=100
    # the Value in 2 position is 4*100=60000+5000+400+30=65430%10--->6543
    return math.floor(abs(num)/pow(10,i))%10
ValueOfIndex2(6543,2)
def countDigit(n):#count digit
    count=0
    while n!=0:
        count+=1
        n//=10
        #n==6542//10==654//2==65//10==6//10==0-->n==0
        #While loop teeminates
    return count
countDigit(6542)

def mostDigits(listValue):
    maximum=0
    for i in range(len(listValue)):
        val=listValue[i]
        maxValue=countDigit(val)
        maximum=max(maximum,maxValue)
    return maximum
listValue=[3,664,21345,56216]
mostDigits(listValue)
