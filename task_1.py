import random
import timeit

def merge_sort (arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge (left, right):
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

def insertion_sort (arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def generate_data(size):
    return [random.randint(0, 10000) for _ in range(size)]

def measure_time(sort_func, data):
    return timeit.timeit(lambda: sort_func(data.copy()), number=1)

sizes = [100, 1000, 5000, 10000]

results = {}

for size in sizes:
    data = generate_data(size)
    
    merge_sort_time = measure_time(merge_sort, data)
    insertion_sort_time = measure_time(insertion_sort, data)
    timsort_time = measure_time(sorted, data)
    
    results[size] = {
        'Merge Sort': merge_sort_time,
        'Insertion Sort': insertion_sort_time,
        'Timsort (sorted)': timsort_time
    }

for size in sizes:
    print(f"Array Size: {size}")
    for sort_type, time_taken in results[size].items():
        print(f"{sort_type}: {time_taken:.6f} seconds")
    print()
