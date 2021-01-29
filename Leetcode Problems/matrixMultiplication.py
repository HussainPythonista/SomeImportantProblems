a=[[1,2,3],
[4,5,6]]
b=[[7,8],
[9,10],[11,12]]
result=[[0,0],
[0,0]]
i=0
print(len(a[0]))
for l in range(len(a[0])):
    print(l)
for i in range(0,len(a)):
    for j in range(len(a)):
        for k in range(len(b)):
          result[i][j]=result[i][j]+a[i][k]*b[k][j]
print(result)