a=[[10,20,40],
   [30,40,30]]
b=[[1,2,4],j
[3,4,6]]
def matrix(value):
    print("Addition of both Matrix is")
    for i in range(len(a)):
        for j in range(len(a[0])):
            
            print(value[0][i][j]+value[1][i][j],end=" ")
        print()
matrix((a,b))

