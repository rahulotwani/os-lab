import os
import time
List=[10,20,30,40,50,60]
sum=0
sub=0
PID=os.fork()
if PID == 0:
    print(PID)
    for i in range(len(List)):
        sum=sum+List[i]
        print("Value of addition = %d, by process with ID : %d"%(sum,os.getpid()))
elif PID>0:
    os.wait()
    print(PID)
    for i in range(len(List)):
        sub=sub-List[i]
        print("Value of substraction = %d by process ID: %d" %(sub,os.getpid()))
else:
    print("Process creation is unsucessful")
print("Thank you")
