from multiprocessing import Process
import random
import time
def p1():
	time.sleep(21)
def p2():
	time.sleep(3)
def p3():
	time.sleep(6)
def p4():
	time.sleep(2)
x1=time.time()
p1=Process(target=p1)
p1.start()
p1.join()
x2=time.time()
print("Turnaround time for the process p1 : ",x2-x1)
print("Waiting time for the process p1 : ",x2-x1 - 21)
w1=x2-x1 - 21
p2=Process(target=p2)
p2.start()
p2.join()
x2=time.time()
print("Turnaround time for the process p2 : ",x2-x1)
print("Waiting time for the process p2 : ",x2-x1 - 3)
w2=x2-x1 - 3
p3=Process(target=p3)
p3.start()
p3.join()
x2=time.time()
print("Turnaround time for the process p3 : ",x2-x1)
print("Waiting time for the process p3 : ",x2-x1 - 6)
w3=x2-x1 - 6
p4=Process(target=p4)
p4.start()
p4.join()
x2=time.time()
print("Turnaround time for the process p4 : ",x2-x1)
print("Waiting time for the process p4 : ",x2-x1 - 2)
w4=x2-x1 - 2
print("Average turnaround time is : ",(((w1+w2+w3+w4)+(21+3+6+2))/4))
print("Average waiting time is : ",(w1+w2+w3+w4)/4)
