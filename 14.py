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
    print("Enter the arrival of the processes :")
    for i in range(n):
        pr.append(int(input()))
        tim=[]
    for i in range(n):
        tim.append(0)
    temp2=[]
    for i in range(n):
        temp2.append(x[i])
    count=n
    i=0
    x1=0
    it=time.time()
    count=n
    while True:
        temp2.sort()
        for i in range(n):
            if temp2[i]!=0:
                p1=Process(target=p, args=(1,))
                temp2[i]-=1
                t1=time.time()
                p1.start()
                p1.join()
                t2=time.time()
                tim[i]+=(t2-t1)
    print(tim)
    print("Turnaround time : ")
    for i in range(n):
        print((tim[i]-pr[i]))
    print("Waiting time :")
    for i in range(n):
        print(tim[i]-pr[i]-temp2[i][1])
fun1()
