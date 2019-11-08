import threading
import time
N = 10
buf = [0] * N
fill_count = threading.Semaphore(0)
empty_count = threading.Semaphore(N)
def producer():
    front = 0
    for i in range(500):
        #print("Item produced ")
        x = 1
        empty_count.acquire()
        buf[front] = x
        fill_count.release()
        front = (front + 1) % N
def consumer():
    rear = 0
    for i in range(500):
        fill_count.acquire()
        y = buf[rear]
        empty_count.release()
        #print("Item consumed ")
        rear = (rear + 1) % N
def fun():
    t1=time.time()
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()
    t2=time.time()
    return(t2-t1)
n=0
for i in range(100):
    n+=fun()
    n/=100
    print("Average difference is",n)