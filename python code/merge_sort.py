#mergesort
import time 
from time import sleep

def mergesort(arr):
    start_time=time.time()
    if len(arr) > 1:
        mid = len(arr) // 2
        leftarray = arr[:mid]
        rightarray = arr[mid:]
        mergesort(leftarray)
        mergesort(rightarray)
        left_index = 0
        right_index = 0
        final_index = 0
        while left_index < len(leftarray) and right_index < len(rightarray):
            if leftarray[left_index] < rightarray[right_index]:
              arr[final_index] = leftarray[left_index]
              left_index = left_index + 1
            else:
                arr[final_index] = rightarray[right_index]
                right_index = right_index + 1
            final_index = final_index + 1
        while right_index < len(rightarray):
            arr[final_index]=rightarray[right_index]
            right_index = right_index + 1
            final_index = final_index + 1
        while left_index < len(leftarray):
            arr[final_index] = leftarray[left_index]
            left_index = left_index + 1
            final_index = final_index + 1
        
    merge_sort_time =time.time() - start_time
    return arr,merge_sort_time