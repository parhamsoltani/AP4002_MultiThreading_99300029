import multiprocessing

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
