#insertion sort
import time
from time import sleep
def insertionsort(arr):
    start_time = time.time()
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[j]
                arr[j]=arr[i]
                arr[i]=temp   
    i=i+1
    insertion_sort_time =time.time() - start_time
    return arr,insertion_sort_time
    