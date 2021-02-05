def BruteForceApproach(array,key):#BigO of N**3
    i=0
    j=0
    value=0

    for i in range(len(array)):
            if value<key:
                value+=array[i]
            if value>key:
                value-=array[j]
                j+=1
            if value==key:
                print("Found")
                break
        
key=8
array=[4,3,2,4,1,3,2,2,2,2]
print(BruteForceApproach(array,key))
#Arrroach 2
def cumulativeSum(array,key):#Big O N**2
    prefix=0
    for i in range(len(array)-1):
        for j in range(i,len(array)):
            prefix+=array[j]
            if prefix==key:
                print(i,j)
def SlidingWindow(array,key):
    binarySearch=[]
    value=0
    for i in range(len(array)-1):
        value+=array[i]+ array[i+1]
        binarySearch.append(value)
    print(binarySearch)
SlidingWindow(array,key)

