import time
import os
import random as rnd 
import sys
from time import sleep
import importlib
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

#now we will start to generate array values and sort them 
choice= int(input("\nHere you have two options:\n 1: Generate random array values... \n 2: Enter array values manually... \n"))
array=[]

if choice==1:
    print("\nEnter new choice: \n 1: Large random values \n 2: Small random values")
    new = int(input())
    if new == 1:
        print("\nEnter length of array you want to generate:")
        length=int(input())
        a = sys.maxsize
        for i in range(length):
            arr = rnd.randint(-a,a)
            array.append(arr)
        print("\nGenerated array elements are given:")
        print(array)
    elif new == 2:
        print("\nEnter length of array you want to generate:")
        length=int(input())
        for i in range(length):
            arr = rnd.randint(-length*10,length*10)
            array.append(arr)
        print("\nGenerated array elements are given:")
        print(array)
    else:
        print("\nPlease enter valid input to proceed:\n")
        sys.exit()

elif choice==2:
    print("\nEnter length of array you want to generate:")
    length = int(input())
    print("\nEnter the array elements:")
    for i in range(0,length):
        arr = int(input())
        array.append(arr)
    print("\nGenerated array elements are given:")
    print(array)
else:
    print("\nPlease enter valid input to proceed:\n")
    sys.exit()
#here I have imported required functions from all the algorithm files for sorting
from insertion_sort import insertionsort
from heap_sort import heapsort,heap
from selection_sort import selectionsort
from bubble_sort import bubblesort
from merge_sort import mergesort
from quick_sort import quicksort,partition
from quick_sort_three_medians import quicksortmed,partition

print("\nSelect any of the following algorithm to calculate running time:\n")
print(" 0: Insertion Sort \n 1: Selection Sort \n 2: Bubble Sort \n 3: Heap Sort  \n 4: Merge Sort \n 5: Quick Sort \n 6: Quick Sort using 3 medians \n 7: Compare every sorting algorithm's running time \n")
select=int(input())
if select==0:
    print("You have selected Insertion sort\n")
    ar,time = insertionsort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort the array by insertion sort: ",time)
elif select==1:
    print("You have selected Selection sort\n")
    ar,time = selectionsort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort the array by selection sort: ",time)
elif select==2:
    print("You have selected Bubble sort\n")
    ar,time = bubblesort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort the array by bubble sort: ",time)
elif select==3:
    print("You have selected Heap sort\n")
    ar,time = heapsort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort the array by heap sort: ",time)
elif select==4:
    print("You have selected Merge sort")
    ar,time = mergesort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort the array by merge sort: ",time)
elif select==5:
    print("You have selected Quick sort")
    ar,time = quicksort(array,0,length-1)
    print("\nSorted array: ",ar)
    print("\nTime to sort the array by quick sort: ",time)
elif select==6:
    print("You have selected Quick sort using 3 medians")
    ar,time=quicksortmed(array,0,length-1)
    print("\nSorted array: ",ar)
    print("\nTime to sort the array by quick sort using 3 medians: ",time)
elif select==7: 
    print("Here all the sorting algorithm's running time will be counted for same array input")
    ar,insertion_time = insertionsort(array)
    ar,selection_time = selectionsort(array)
    ar,bubble_time = bubblesort(array)
    ar,heap_time = heapsort(array)
    ar,merge_time = mergesort(array)
    ar,quick_time = quicksort(array,0,length-1)
    ar,quickmed_time = quicksortmed(array,0,length-1)
    print("\nSorted array:",ar)
    print("\nTime required for each algorithm to sort the array:\n")
    print("1. Insertion sort: ",insertion_time)
    print("2. Selection sort: ",selection_time)
    print("3. Bubble sort: ",bubble_time)
    print("4. Heap sort: ",heap_time)
    print("5. Merge sort: ",merge_time)
    print("6. Quick sort: ",quick_time)
    print("7. Quick sort using 3 medians: ",quickmed_time)
    print("\nTotal time required to run all algorithms: ",insertion_time+selection_time+bubble_time+merge_time+quick_time+quickmed_time)
    #let's compare which algorithm requires minimum time

    dict={}
    dict[insertion_time]='Insertion sort'
    dict[selection_time]='Selection sort'
    dict[bubble_time]='Bubble sort'
    dict[heap_time]='Heap sort'
    dict[merge_time]='Merge sort'
    dict[quick_time]='Quick sort'
    dict[quickmed_time]='Quick sort using 3 medians'
    time_list=[]
    time_list.append(insertion_time)
    time_list.append(selection_time)
    time_list.append(bubble_time)
    time_list.append(heap_time)
    time_list.append(merge_time)
    time_list.append(quick_time)
    time_list.append(quickmed_time)
    min_time = min(time_list)
    max_time = max(time_list)
    print("\nFor {} inputs {} runs in MINIMUM time".format(length,dict[min_time]))
    print("\nAnd {} takes MAXIMUM time to run!!!\n".format(dict[max_time]))

else:
    print("Invalid choice! Try again...")
    sys.exit()

print("If you want to generate graph then press 1 or press any other key to exit")
graph_input = int(input())
if graph_input != 1:
    sys.exit()
else:
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
            arr = rnd.randint(-length,length) #generating array for certain different lengths
            array.append(arr)
        print(array)
        #calculating time for each and everysorting and appending to respective sorting's time list
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
