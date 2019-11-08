from multiprocessing import Process
import random
import time
def p(t):
    time.sleep(t)
def fun1():
    print("Enter the number of processes :")
    n=int(input())
    x=[]
    print("Enter the burst times of the processes :")
    for i in range(n):
        x.append(int(input()))
    pr=[]
    print("Enter the priority of the processes :")
    for i in range(n):
        pr.append(int(input()))
        tim=[]
    for i in range(n):
        tim.append(0)
    temp2=[]
    for i in range(n):
        temp1=[]
        temp1.append(pr[i])
        temp1.append(x[i])
        temp2.append(temp1)
    temp2.sort()
    count=n
    i=0
    x1=0
    it=time.time()
    for i in range(n):
        p1=Process(target=p, args=(temp2[i][1],))
        t1=time.time()
        p1.start()
        p1.join()
        t2=time.time()
        tim[i]+=(t2)
    print("Turnaround time : ")
    avgt=0
    for i in range(n):
        print(tim[i]-it)
        avgt+=(tim[i]-it)
    print(avgt/4)
    print("Waiting time :")
    avgw=0
    for i in range(n):
        print(tim[i]-it-temp2[i][1])
        avgw+=(tim[i]-it-temp2[i][1])
    print(avgw/4)
fun1()
