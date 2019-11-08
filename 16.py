import multiprocessing
import time
 
def last(n):
    return n[1]
   
def timeTaken():
    time.sleep(1)
   
#pr=[[0,21],[1,3],[2,6],[3,2]]
pr=[0,1,2,3]
bt=[21,6,3,2]
rbt=[21,6,3,2]
ar=[0,1,2,3]
n=len(pr)
tat=[0]*n
wt=[0]*n
WtTime=0
TaTime=0
sTime=time.time()
t=0
pStart=[-1]*n
while 1:
    q=[]
    for i in range(len(ar)):
        if ar[i]<=t and rbt[i]>0:
            tup=pr[i],rbt[i]
            q.append(tup)
    if len(q)==0:
        break
    q.sort(key=lambda x:x[1])
    p=multiprocessing.Process(target=timeTaken,args=())
    if(pStart[q[0][0]])==-1:
        pStart[q[0][0]]=time.time()
    p.start()
    p.join()
    rbt[q[0][0]]-=1
    if(rbt[q[0][0]]==0):
        tat[q[0][0]]=time.time()-pStart[q[0][0]]
        wt[q[0][0]]=tat[q[0][0]]-bt[q[0][0]]
    t+=1
print("Waiting Time"+" Turnaround Time")
for i in range(n):
    print(str(wt[i])+" "+str(tat[i]))
    WtTime+=wt[i]
    TaTime+=tat[i]
print("Average waiting time: ",WtTime/n)
print("Average turnaround time: ",TaTime/n)
