import multiprocessing
import time
def producer(product,lock):
	for i in range(500):
		lock.acquire()
		#print("Item produced")
		product.value=product.value+1
		lock.release()
def consumer(product,lock):
	for i in range(500):
		lock.acquire()
		#print("Item consumed")
		product.value=product.value-1
		lock.release()
def fun():
	t1=time.time()
	product=multiprocessing.Value('i',100)
	lock=multiprocessing.Lock()
	p=multiprocessing.Process(target=producer,args=(product,lock,))
	c=multiprocessing.Process(target=consumer,args=(product,lock,))
	p.start()
	c.start()
	p.join()
	c.join()
	t2=time.time()
	return(t2-t1)
if __name__=="__main__":
	n=0
	for i in range(100):
		n+=fun()
		print("Time taken",n/100)