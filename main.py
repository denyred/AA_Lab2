# This is a sample Python script.
import random
import time
import matplotlib.pyplot as plt

def create_vector(n):
    """
    Creates a vector of length n with random integer values.
    """
    return [random.randint(0, 100) for i in range(n)]

def quick_sort(vector):
    """
    Sorts a vector using the quicksort algorithm.
    """
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[0]
        left = []
        right = []
        for i in range(1, len(vector)):
            if vector[i] < pivot:
                left.append(vector[i])
            else:
                right.append(vector[i])
        return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(vector):
    """
    Sorts a vector using the merge sort algorithm.
    """
    if len(vector) > 1:
        mid = len(vector) // 2
        left_half = vector[:mid]
        right_half = vector[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vector[k] = left_half[i]
                i += 1
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            vector[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            vector[k] = right_half[j]
            j += 1
            k += 1

def heap_sort(vector):
    """
    Sorts a vector using the heapsort algorithm.
    """
    n = len(vector)
    for i in range(n // 2 - 1, -1, -1):
        heapify(vector, n, i)
    for i in range(n - 1, 0, -1):
        vector[0], vector[i] = vector[i], vector[0]
        heapify(vector, i, 0)

def heapify(vector, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and vector[largest] < vector[left]:
        largest = left
    if right < n and vector[largest] < vector[right]:
        largest = right
    if largest != i:
        vector[i], vector[largest] = vector[largest], vector[i]
        heapify(vector, n, largest)

def selection_sort(vector):
    """
    Sorts a vector using the selection sort algorithm.
    """
    n = len(vector)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if vector[j] < vector[min_idx]:
                min_idx = j
        vector[i], vector[min_idx] = vector[min_idx], vector[i]

def compare_sorting_algorithms(n):
    """
    Compares the speed of four sorting algorithms by measuring the time taken
    to sort a vector of length n using each algorithm. Returns a plot of the results.
    """
    vector = create_vector(n)
    quick_sort_time = time.time()
    quick_sort(vector)
    quick_sort_time = time.time() - quick_sort_time
    vector = create_vector(n)
    merge_sort_time = time.time()
    merge_sort(vector)
    merge_sort_time = time.time() - merge_sort_time
    vector = create_vector(n)
    selection_sort_time = time.time()
    selection_sort(vector)
    selection_sort_time = time.time() - selection_sort_time
    vector = create_vector(n)
    heap_sort_time = time.time()
    heap_sort(vector)
    heap_sort_time = time.time() - heap_sort_time
    plt.bar(['Selection Sort', 'Heap Sort','Quick Sort', 'Merge Sort'], [selection_sort_time, heap_sort_time, quick_sort_time,merge_sort_time])
    plt.title('Sorting Algorithm Comparison')
    plt.ylabel('Time Taken (seconds)')
    plt.show()

compare_sorting_algorithms(10000)