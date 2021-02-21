def Palindrome(string):
        if len(string)>1:
            string=string.lower()
            reverse=string[::-1]
            if string==reverse:
                
                return True
            else:
                return False
def Execution(s):
        if len(s)>0:
            subString=""
            bPoint=0
            aPoint=0
            while len(s)>bPoint:
                subString+=s[bPoint+aPoint] 
                print(subString)
                pal=Palindrome(subString)
                bPoint+=1
                if not pal :
                    print(bPoint)
                    s=s.replace(s[aPoint],"",1)
                    
                    return Exception(s)
                if pal:
                    return pal
                    aPoint+=1
                
        else:
            return False
def longestPalindrome(s):
    start=0
    end=len(s)-1
    subString=""
    while start<end:
        if s[start]==s[end] and s[start+1]==s[end-1]:
            subString+=s[start]+s[end]
            print(subString)
            start+=1
            end-=1
        start+=1
        end-=1
print(longestPalindrome("malayalam"))
        
        
        