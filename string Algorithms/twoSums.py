nums = [11,15,2,7]
target = 9
i=0
j=0
value=0
for _ in range(len(nums)):
    if value<target:
        value+=nums[i+j]
        i+=1
    if value>target:
        value-=nums[j]
        j+=1
    if value==target:
        print(j,i)