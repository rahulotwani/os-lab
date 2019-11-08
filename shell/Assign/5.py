import os
import time
print("Enter the size of the matrices :")
n=int(input())
print("Enter the elements of the first matrix :")
a=[]
a1=[]
for i in range(0,n):
    a1=[]
    for j in range(0,n):
        a1.append(int(input()))
    a.append(a1)
print("Enter the elements of the second matrix :")
b=[]
b1=[]
for i in range(0,n):
    b1=[]
    for j in range(0,n):
        b1.append(int(input()))
    b.append(b1)
print("Matrix 1:")
for i in range(n):
    print(a[i])
print("Matrix 2:")
for i in range(n):
    print(b[i])
PID=os.fork()
if PID==0:
    PID=os.fork()
    if PID==0:
        PID=os.fork()
        if PID==0:
            print("Adding")
            c=[[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    c[i][j]=a[i][j]+b[i][j]
            for i in range(n):
                print(c[i])
               
        else:
            os.wait()
            print("Substracting")
            c=[[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    c[i][j]=a[i][j]-b[i][j]
            for i in range(n):
                print(c[i])
    else:
        os.wait()
        print("Multiplying")
        c=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n): 
                    c[i][j] += a[i][k] * b[k][j]
        for i in range(n):
            print(c[i])
else:
    os.wait()
