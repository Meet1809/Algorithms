#heap sort
import time
from time import sleep

def heap(arr,length,index):
    max = index
    left_child = 2*index+1
    right_child = 2*index+2
    if left_child < length and arr[index] < arr[left_child]:
        max = left_child
    if right_child < length and arr[max] < arr[right_child]:
        max = right_child
    if max != index:
        temp = arr[max]
        arr[max] = arr[index]
        arr[index] = temp
        heap(arr,length,max)

def heapsort(arr):
    start_time = time.time()
    length = len(arr)
    x=length+1
    for i in reversed(range(x)):
        heap(arr,length,i)

    for i in reversed(range(length)):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        heap(arr,i,0)       

    heap_sort_time =time.time() - start_time
    return arr, heap_sort_time
    