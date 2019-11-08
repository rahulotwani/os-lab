import os
import time
PID=os.fork()
if PID == 0:
    a=[]
    a.append(0)
    a.append(1)
    n1=0
    n2=1
    n3=0
    while(n3<=100):
        n3=n2+n1
        if(n3<=100):
            a.append(n3)
        n1=n2
        n2=n3
    print("Fibonacci Series :")
    print(a)
else:
    os.wait()
    time.sleep(1)
    a=[]
    for i in range(1,101):
        a.append(i)
    print("Natural Numbers :") 
    print(a)
