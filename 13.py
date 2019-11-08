from multiprocessing import Process
import random
import time
def p(t):
    time.sleep(t)
def fun1():
    print("Enter the number of processes :")
    n=int(input())
    x=[]
    z1=[]
    print("Enter the burst times of the processes :")
    for i in range(n):
        inpu=int(input())
        x.append(inpu)
        z1.append(inpu)
    print("Enter the CPU time slot :")
    y=int(input())
    tim=[]
    for i in range(n):
        tim.append(0)
    count=n
    i=0
    x1=0
    it=time.time()
    while count>0:
        if x[i] != 0:
            if x[i] > y:
                x[i]-=y
                x1=y
            else:
                x1=x[i]
                x[i]=0
                count-=1
            p1=Process(target=p, args=[x1,])
            t1=time.time()
            p1.start()
            p1.join()
            t2=time.time()
            print("Executed : ",i)
            print("for : ",(t2-t1))
            tim[i]=(t2)
        i+=1
        if i==n:
            i=0
    avgt=0
    for i in range(n):
        tim[i]-=it
        avgt+=tim[i]
    print("Turnaround time :",tim)
    print("Average : ",avgt/4)
    avgt=0
    for i in range(n):
        tim[i]-=z1[i]
        avgt+=tim[i]
    print("Waiting time is : ",tim)
    print("Average : ",avgt/4)
fun1()
