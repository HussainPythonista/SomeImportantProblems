

def Condition(x):
    minValue=-2**31
    maxValue=2**31-1

    if x<minValue or x>maxValue:
        return 0


def negative(x):
    x=x*-1
    s=str(x)
    s=int(s[::-1])
    s=s*-1
    return s
def positive(x):
    s=str(x)
    s=s[::-1]
    s=int(s)
    return s
def reverseValue(x):
    if x<0:
        value=negative(x)
        if value<=-2**31:
            return 0
    else:
        value=positive(x)
        if value>=2**31:
            return 0
x=-1534236469  
print(reverseValue(x))




def reverse(self, x: int) -> int:
        maxNumber=2**31-1#32Bit
        minNumber=-2**31#32Bit in negative side
        res=0
        negative=False
        if x<0:
            x=x*-1
            negative=True
        while x>0:
            pop=x%10
            x//=10
            res=res*10+pop
            if res<minNumber or res>maxNumber:
                return 0
        if negative==True:
            res=res*-1
        return res