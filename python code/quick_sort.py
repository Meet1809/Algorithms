import time
from time import sleep
def partition(arr,low,high):
    pivot = arr[high] 
    #taking the last element as pivot
    first = low-1
    for i in range(low,high):
        if arr[i] <= pivot:
            first =first + 1
            temp = arr[first]
            arr[first] = arr[i]
            arr[i] = temp
            #exchanging two items 
    temp = arr[first+1]
    arr[first+1] = arr[high]
    arr[high] = temp
    #exchanging pivot element and first pointer as first gets bigger than right pointer
    return first+1

def quicksort(arr,low,high):
    start_time = time.time()
    if low<high:
        length = partition(arr,low,high)
        quicksort(arr,low,length-1)
        quicksort(arr,length+1,high)
    quick_sort_time = time.time() - start_time
    return arr,quick_sort_time
