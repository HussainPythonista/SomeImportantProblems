def powofn(a, n):#Divide And Conqure
    if n == 0:
        return 1
    if n%2==1:
        return powofn(a, n//2) * powofn(a, n//2)*a
    if n%2==0:
        return powofn(a, n//2) * powofn(a, n//2)
    
#Dynamic Programming
def dyNamicPow(a,n):#It is Efficient one
    if n==0:
        return 1
    if n%2==1:
        half=powofn(a, n//2)#We doesnt return and multiply the Function
        #We store the variable in function and only multiply variable
        return half*half*a
    if n%2==0:
        half=powofn(a, n//2)
        return half*half
print(dyNamicPow(2,5))
    