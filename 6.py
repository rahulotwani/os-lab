import multiprocessing
def withdraw(balance,lock):
	for i in range(10000):
		lock.acquire()
		balance.value=balance.value-5
		lock.release()
def deposit(balance,lock):
	for i in range(10000):
		lock.acquire()
		balance.value=balance.value+4
		lock.release()
def perform_transaction():
	balance=multiprocessing.Value('i',100)
	lock=multiprocessing.Lock()
	p1=multiprocessing.Process(target=withdraw,args=(balance,lock,))
	p2=multiprocessing.Process(target=deposit,args=(balance,lock,))
	p1.start()
	p1.join()
	p2.start()
	p2.join()
	print("Final balance is :",balance.value)
if __name__=="__main__":
	for _ in range(10):
		perform_transaction()