from multiprocessing import Process
import os
import time
def sleeper(name,seconds):
    print('starting child process with id:')
    print('parent process : ',os.getppid())
    print('sleeping for %s' %seconds)
    time.sleep(seconds)
    print("Done sleeping")
print(" in parent process(id %s)"%os.getppid())
p=Process(target=sleeper,args=('bob',5))
p.start()
print("in parent process after child process starts")
print("parent process about to join child process")
p.join()
print("in parent process after child process join")
print("parent process exiting with id", os.getpid())
print("the parent's parent process :",os.getppid())


