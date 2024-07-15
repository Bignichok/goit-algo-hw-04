import heapq

# O(N log N)

def merge_k_lists(lists):
    result = []
    for list in lists:
        result += list
    print(result)
    
    return sorted(result)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)


# O(N log K) - має показувати себе ефективніше при великій к-ті масивів
def optimized_merge_k_lists(lists):
    min_heap = []
    
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i, 0))
    
    result = []
    
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)
        
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
    
    return result

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = optimized_merge_k_lists(lists)
print("Відсортований список:", merged_list)




