#selection sort
import time
from time import sleep
def selectionsort(arr):
    start_time = time.time()
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    selection_sort_time =time.time() - start_time
    return arr, selection_sort_time