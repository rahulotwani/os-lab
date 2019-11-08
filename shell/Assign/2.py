import os
import time
PID = os.fork()
if PID == 0:
    print("Enter first number :")
    n1=int(input())
    print("Enter second number : ")
    n2=int(input())
    print("Addition :",n1+n2)
    print("Substration :",n1-n2)
    print("Multiplication :",n1*n2)
    print("Division :",n1//n2)
else:
    os.wait()
