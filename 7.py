import multiprocessing
import os
import time
def cal0():
	c=0
	for i in range(1000):
		c+=1
def cal1():
	c=0
	for i in range(500):
		c+=1
def cal2():
	c=0
	for i in range(500):
		c+=1
def perform_transaction():
	p0=multiprocessing.Process(target=cal0,args=())
	p1=multiprocessing.Process(target=cal1,args=())
	p2=multiprocessing.Process(target=cal2,args=())
	t0=time.time()
	p0.start()
	p0.join()
	t1=time.time()
	t2=time.time()
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	t3=time.time()
	print("First time is :",t1-t0)
	print("Second case time is :",t3-t2)
perform_transaction()