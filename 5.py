import multiprocessing
def withdraw(balance):
	for _ in range(10000):
		balance.value=balance.value-5
	print("W")
def deposit(balance):
	for _ in range(10000):
		balance.value=balance.value+4
	print("D")
def perform_transaction():
	balance=multiprocessing.Value('i',100)
	p1=multiprocessing.Process(target=withdraw,args=(balance,))
	p2=multiprocessing.Process(target=deposit,args=(balance,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	print("Final balance is :",balance.value)
if __name__=="__main__":
	for _ in range(10):
		perform_transaction()
		#print("bal=",bal)