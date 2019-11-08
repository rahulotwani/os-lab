import os
import time

print("Enter the size of the first list : ")
n1=int(input())
print("Enter the numbers to be inserted : ")
a=[]
for i in range(0,n1):
    a.append(int(input()))

print("Enter the size of the second list : ")
n2=int(input())
print("Enter the numbers to be inserted : ")
b=[]
for i in range(0,n2):
    b.append(int(input()))

PID= os.fork()
if PID==0:
    a.sort()
else:
    os.wait()
    PID=os.fork()
    if PID==0:
        b.sort()
    else:
        os.wait()
        c=[]
        j=0
        k=0
        while(j<n1 and k<n2):
            if(a[j]>b[k]):
                c.append(b[k])
                k+=1
            else:
                c.append(a[j])
                j+=1
        for i in range(j,n1):
            c.append(a[j])
        for i in range(k,n2):
            c.append(b[k])
        print(c)
