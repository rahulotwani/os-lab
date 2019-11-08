from multiprocessing import Process
import manager
def f(d,l):
	d[1]='1'
	d['2']=5
	d[0.25]=None
	l.reverse()
	print(d)
	print(l)

if __name__=="__main__":
	manager=Manager()
	d=manager.dict()
	l=manager.list(range(10))
	p=Process(target=f,args=(d,l))
	p=start()
	p.join()
	d[1]='1'
	d['2']=5
	d[0.25]=4
	print(d)
	print(l)