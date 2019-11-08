import os
from multiprocessing import Process

result=[]
def squarevalue(List):
	for i in List:
		result.append(i*i)
	print("Inside function :")
	print(result)

List=[9,8,7,6,5,4,3,2,1] 
p=Process(target=squarevalue,args=(List,))
p.start()
print("Outside function :")
print(result)