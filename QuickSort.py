import threading
import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    greater = quicksort([x for x in arr[1:] if x >= pivot])
    return lesser + [pivot] + greater

def threaded_quicksort(arr, depth=0, max_depth=2):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser = [x for x in arr[1:] if x < pivot]
    greater = [x for x in arr[1:] if x >= pivot]

    if depth < max_depth:
        left_thread = threading.Thread(target=lambda: lesser.__setitem__(slice(None), threaded_quicksort(lesser, depth+1)))
        right_thread = threading.Thread(target=lambda: greater.__setitem__(slice(None), threaded_quicksort(greater, depth+1)))

        left_thread.start()
        right_thread.start()
        left_thread.join()
        right_thread.join()

    else:
        lesser = threaded_quicksort(lesser, depth+1)
        greater = threaded_quicksort(greater, depth+1)

    return lesser + [pivot] + greater

if __name__ == "__main__":
    data = [random.randint(0, 1000) for _ in range(10000)]
    data_copy = data[:]

    start = time.time()
    quicksort(data)
    print("Single-threaded quicksort:", time.time() - start, "seconds")

    start = time.time()
    threaded_quicksort(data_copy)
    print("Multi-threaded quicksort:", time.time() - start, "seconds")
