import threading
import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def threaded_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    t1 = threading.Thread(target=lambda: left.__setitem__(slice(None), threaded_merge_sort(left)))
    t2 = threading.Thread(target=lambda: right.__setitem__(slice(None), threaded_merge_sort(right)))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    return merge(left, right)

if __name__ == "__main__":
    data = [random.randint(0, 1000) for _ in range(10000)]
    data_copy = data[:]

    start = time.time()
    merge_sort(data)
    print("Single-threaded merge sort:", time.time() - start, "seconds")

    start = time.time()
    threaded_merge_sort(data_copy)
    print("Multi-threaded merge sort:", time.time() - start, "seconds")
