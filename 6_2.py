import multiprocessing
def withdraw(conn):
	balance=conn.recv()
	for i in range(10000):
		balance=balance-1
	conn.send(balance)
def deposit(conn):
	balance=conn.recv()
	for i in range(10000):
		balance=balance+1
	conn.send(balance)
def perform_transaction():
	p1_conn,p2_conn=multiprocessing.Pipe()
	p1=multiprocessing.Process(target=withdraw,args=(p2_conn,))
	p2=multiprocessing.Process(target=deposit,args=(p2_conn,))
	p1_conn.send(100)
	p1.start()
	p1.join()
	n=p1_conn.recv()
	print("bal",n)
	p1_conn.send(n)
	p2.start()
	p2.join()
	print("Final balance is :",p1_conn.recv())
if __name__=="__main__":
	for i in range(10):
		perform_transaction()