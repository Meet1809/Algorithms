import time
import os
import random as rnd 
import sys
from time import sleep
import importlib
import matplotlib.pyplot as plt
from insertion_sort import insertionsort
from heap_sort import heapsort,heap
from selection_sort import selectionsort
from bubble_sort import bubblesort
from merge_sort import mergesort
from quick_sort import quicksort,partition
from quick_sort_three_medians import quicksortmed,partition
sys.setrecursionlimit(10000)

iter_num = int(input("Enter number of iterations: "))
length = 3
input_sizes =[]
insertion = []
selection = []
bubble = []
heap = []
array = []
merge = []
quick = []
quickmed = []
for i in range(iter_num):
    for a in range(length):
        arr = rnd.randint(-length*10,length*10)
        array.append(arr)
    ar, insertion_time = insertionsort(array)
    insertion.append(insertion_time)
    ar, selection_time = selectionsort(array)
    selection.append(selection_time)
    ar, bubble_time = bubblesort(array)
    bubble.append(bubble_time)
    ar, heap_time = insertionsort(array)
    heap.append(heap_time)
    ar, merge_time = mergesort(array)
    merge.append(merge_time)
    ar,quick_time = quicksort(array,0,len(array)-1)
    quick.append(quick_time)
    ar,quickmed_time = quicksortmed(array,0,len(array)-1)
    quickmed.append(quickmed_time)
    input_sizes.append(length)
    length = length * 3

print("Input sizes: ",input_sizes)

plt.plot(input_sizes,insertion,label="Insertion sort")
plt.plot(input_sizes,selection,label="Selection sort")
plt.plot(input_sizes,bubble,label="Bubble sort")
plt.plot(input_sizes,heap,label="Heap sort")
plt.plot(input_sizes,merge,label="Merge sort")
plt.plot(input_sizes,quick,label="Quick sort")
plt.plot(input_sizes,quickmed,label="Quick sort 3 medians")
plt.xlabel("Input Size")
plt.ylabel("Time")
plt.legend()
plt.show()
sys.exit()
