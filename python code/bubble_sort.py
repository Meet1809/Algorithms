#bubble sort
import time
from time import sleep
def bubblesort(arr):
    start_time=time.time()
    for j in range(len(arr)):
        for i in range(len(arr)-j-1):
            if arr[i]>arr[i+1]:
                arr[i+1],arr[i]=arr[i],arr[i+1]
        i=i+1
    bubble_sort_time =time.time() - start_time
    return arr,bubble_sort_time