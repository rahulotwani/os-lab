from multiprocessing import Process
import random
import time
def p(t):
	time.sleep(t)
print("Enter the burst times : ")
x=[]
for i in range(4):
	x.append(int(input()))
x.sort()
x1=time.time()
p1=Process(target=p, args=(x[0],))
p1.start()
p1.join()
x2=time.time()
print("Turnaround time for the process p1 : ",x2-x1)
print("Waiting time for the process p1 : ",x2-x1 - x[0])
w1=x2-x1 - 21
p2=Process(target=p,args=(x[1],))
p2.start()
p2.join()
x2=time.time()
print("Turnaround time for the process p2 : ",x2-x1)
print("Waiting time for the process p2 : ",x2-x1 - x[1])
w2=x2-x1 - 3
p3=Process(target=p,args=(x[2],))
p3.start()
p3.join()
x2=time.time()
print("Turnaround time for the process p3 : ",x2-x1)
print("Waiting time for the process p3 : ",x2-x1 - x[2])
w3=x2-x1 - 6
p4=Process(target=p,args=(x[3],))
p4.start()
p4.join()
x2=time.time()
print("Turnaround time for the process p4 : ",x2-x1)
print("Waiting time for the process p4 : ",x2-x1 - x[3])
w4=x2-x1 - 2
print("Average turnaround time is : ",(((w1+w2+w3+w4)+(x[0]+x[1]+x[2]+x[3]))/4))
print("Average waiting time is : ",(w1+w2+w3+w4)/4)
