import multiprocessing
import time 
import random 

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        left = mergeSort(L)
        right = mergeSort(R)
        return merge(left, right)
    return arr

def merge(L, R):
    i = j = k = 0
    merge = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            merge.append(L[i])
            i += 1
        else:
            merge.append(R[j])
            j += 1
        k += 1
    while i < len(L):
        merge.append(L[i])
        i += 1
        k += 1
    while j < len(R):
        merge.append(R[j])
        j += 1
        k += 1
    return merge

def parallel(numbers):
    n = len(numbers)
    data = [numbers[0:n//2],numbers[n//2:]]
    pool = multiprocessing.Pool(processes=2)
    data = pool.map(mergeSort, data)
    merge(data[0], data[1])

if __name__ == '__main__':
    arr = [random.randint(0, 10**8) for _ in range(100000)]
    parallel_start_time = time.perf_counter()
    parallel(arr)
    parallel_end_time = time.perf_counter()
    typical_start_time = time.perf_counter()
    mergeSort(arr)
    typical_end_time = time.perf_counter()
    print(f"MergeSort: {typical_end_time - typical_start_time}")
    print(f"Parallel MergeSort: {parallel_end_time - parallel_start_time}")
