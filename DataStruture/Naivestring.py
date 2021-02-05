a="ABCBBAABA"
b="BBA"
count=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i+j]!=b[j]:
            print(a[i+j],b[j])
            break  
        elif len(b)-1==j:
            print(a[len(b)-1],a[j])
            print("Between this Index",i,"to",i+len(b))
        
        
    
                
        
       
                

        