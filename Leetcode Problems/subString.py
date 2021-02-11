from typing import no_type_check


def lengthOfLongestSubstring(s):
    leftPointer=0
    rightPointer=0
    value=[]
    maxValue=0
    for _ in range(len(s)+1):
        if s[rightPointer] not in value:
            
            value.append(s[rightPointer])
            rightPointer+=1
            print(value)
            maxValue=max(maxValue,len(value))
        else:
            value.remove(s[leftPointer])
            leftPointer+=1
    return maxValue
s = "pwwkew"
print(lengthOfLongestSubstring(s))
        