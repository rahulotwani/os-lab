import time
import os
from multiprocessing import Process
import random

def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
def f(arr):
	file2=open("2.txt",'a')
	t1=time.time()
	mergeSort(arr)
	t2=time.time()
	file2.write(str(t2-t1)+"\n")
	file2.close()
	#print("Time taken by the child : ",t2-t1)

k=0
while(k<100):
	arr = []
	n = 100000
	t1=time.time()
	for i in range(n):
		arr.append(random.randint(1,1000000))
	t2=time.time() 

	p=Process(target=f,args=(arr,))
	p.start()
	t3=time.time()
	mergeSort(arr)
	t4=time.time()
	file1=open("1.txt",'a')
	file1.write(str(t4-t3)+"\n")
	file1.close()
	k+=1
	#arr.sort()
	#print("Time taken for the array generation : ",t2-t1)
	#print("Time taken for sorting in the parent process : ",t4-t3)
file1=open('1.txt','r')
file2=open('2.txt','r')
array1=[]
for line in file1: # read rest of lines
	array1.append([float(x) for x in line.split()])
array2=[]
for line1 in file2: # read rest of lines
	array2.append([float(x) for x in line1.split()])
k=0.0
k1=0.0
for i in range(100):
	k+=array1[i][0]
	k1+=array2[i][0]
print(k1//100)
print(k2//100)