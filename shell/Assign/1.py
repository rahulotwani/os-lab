import os
import time
PID = os.fork()
if PID == 0:
    time.sleep(30)
    print("terminating child")
else:
    os.wait()
    time.sleep(20)
    print("terminating parent")