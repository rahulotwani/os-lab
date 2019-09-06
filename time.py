import os
import time
import multiprocessing
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
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
  

def f(arr):
    t1=time.time()
    mergeSort(arr)
    t2=time.time()
    print("Time taken by child process=",t2-t1)


t1=time.time()
arr = [] 
n = 100000
for i in range(n):
    arr.append(random.randint(1,1000000)) 
p=multiprocessing.Process(target=f,args=(arr,))
p.start()
t2=time.time()
#arr.sort() 
mergeSort(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i])

print("time taken for array generation:",t2-t1)

