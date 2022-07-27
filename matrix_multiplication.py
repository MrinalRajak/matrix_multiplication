

#Determination of matrix multiplication
a=[]
m=int(input("Enter the no.of rows of matrix a: "))
n=int(input("Enter the no.of columns of matrix a: "))
a=[[int(input())for i in range(n)]for j in range(m)]

print("The matrix a: ",a)

b=[]
p=int(input("Enter the no.of rows of matrix b: "))
q=int(input("Enter the no.of rows of matrix b: "))
b=[[int(input())for i in range(q)]for j in range(p)]

print("The matrix b: ",b)

c=[[0]*q for i in range(m)]
print("The Null matrix: ",c)


if(n==p):
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
else:
    print("matrices are not conformal for multiplication")
print("The resultant matrix: ",c)
            
