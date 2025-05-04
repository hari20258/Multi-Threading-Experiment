# Multi-Threading-Experiment
🧵 Python Multithreading experiment — Simple Code Explanation
This project contains 3 Python programs that use threads to make the computer do multiple things at the same time. This helps make sorting or downloading faster.

✅ 1. Multi-threaded Merge Sort — merge_sort_threaded.py
🔍 What It Does:
It sorts a list of numbers using the merge sort algorithm.

Uses Python threads to split the work and sort faster.

🧠 Code Summary:
def merge_sort(arr): ...
Regular merge sort: splits the list, sorts each half, and merges.

def threaded_merge_sort(arr): ...
Uses two threads to sort left and right parts at the same time.

t1 = threading.Thread(...)
t2 = threading.Thread(...)
These lines create threads that do sorting in parallel.

t1.start(); t2.start(); t1.join(); t2.join()
Starts the threads and waits for them to finish before merging.

print("Time taken...")
Compares time between single-threaded and multithreaded versions.

✅ 2. Multi-threaded Quicksort — quicksort_threaded.py
🔍 What It Does:
Sorts a list using quicksort, another fast sorting method.

Uses threads to sort the smaller parts concurrently.

🧠 Code Summary:
def quicksort(arr): ...
Regular quicksort: chooses a pivot and sorts items smaller or larger than it.

def threaded_quicksort(arr, depth=0, max_depth=2): ...
Uses threads only up to a certain depth to avoid using too many threads.

left_thread = threading.Thread(...)
right_thread = threading.Thread(...)
Sorts the two sides of the list at the same time.

if depth < max_depth: ...
Controls how many layers of sorting use threads (to avoid crashes).

✅ 3. Concurrent File Downloader — concurrent_file_downloader.py
🔍 What It Does:
Downloads 3 image files from the internet.

First does it one by one (slow).

Then uses threads to download all at the same time (fast).

🧠 Code Summary:

def download_file(url, filename): ...
Downloads one file and saves it with a proper name.

def sequential_download(urls): ...
Downloads files one after the other (no threads).

def threaded_download(urls): ...
Creates a thread for each file download.

t.start(); threads.append(t); t.join()
Starts all download threads and waits until all are done.

print("Time taken...")
Shows how much time each method takes.


🚀 What You Learn from This Project
🔄 How to use Python's threading module.

⏱️ How multithreading makes tasks faster.

🧠 How sorting and downloading can be optimized.

⚠️ Why controlling threads (like in quicksort) is important for performance.
