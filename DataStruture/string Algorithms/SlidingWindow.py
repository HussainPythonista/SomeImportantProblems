#NaiveApproach

def NaiveApproachh(a, b):
    maxValue=0
    i=0
    while i<len(a)-b+1:
        for j in range(b):
            print(a[i]+a[i+j])
        i+=1


#Sliding Window Aproach
def slidingWindow(array,Value):
    window=0
    maxValue=window
    maxValue=sum(array[:Value])
    window=maxValue
    for slide in range(Value,len(array)):
        #print(array[slide])
        temp=window-array[slide-Value]
        window=temp+array[slide]
        maxValue=max(maxValue,window)
        print(maxValue)
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
print(contineousLongestString(array))


