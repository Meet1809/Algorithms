#quicksort median of three item as pivot
import time
from time import sleep

def find_pivot(arr,low,high):
    mid = (low+high)//2
    if arr[low]<=arr[mid]:
        if arr[mid]<=arr[high]:
            pivot = arr[mid]
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
        elif arr[mid] > arr[high]:
            if arr[high] > arr[low]:
                pivot = arr[high]
            else:
                pivot = arr[low]
                temp = arr[low]
                arr[low] = arr[high]
                arr[high] = temp
    else:
        if arr[mid] > arr[high]:
            pivot = arr[mid]
            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
        elif arr[high] > arr[mid]:
            if arr[high] <= arr[low]:        
                pivot = arr[high]
                temp = arr[low]
                arr[low] = arr[mid]
                arr[mid] = temp
            else:
                pivot = arr[low]
                temp = arr[high]
                arr[high] = arr[low]
                arr[low] = arr[mid]
                arr[mid] = temp
    return pivot

def partition(arr,low,high):
    pivot = find_pivot(arr,low,high)
    first = low-1
    for i in range(low,high):
        if arr[i]<=pivot:
            first = first + 1
            temp = arr[first]
            arr[first] = arr[i]
            arr[i] = temp
    temp = arr[first+1]
    arr[first+1] = arr[high]
    arr[high] = temp
    return first+1

def quicksortmed(arr,low,high):
    start_time = time.time()
    if low<high:
        length = partition(arr,low,high)
        quicksortmed(arr,low,length-1)
        quicksortmed(arr,length+1,high)
    quick_sort_time = time.time() - start_time
    return arr,quick_sort_time
