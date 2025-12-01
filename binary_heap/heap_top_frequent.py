# Top K Frequent Elements Count elements, build a heap of pairs (frequency, element).
import heapq
from collections import Counter


def top_frequent_items(arr, n):

    counter_freq = Counter(arr)
    min_heap = []

    for key, value in counter_freq.items():
        heapq.heappush(min_heap, (value, key)) # Each heappush O(log n) => total O (n log n)

        if len(min_heap) > n:
            heapq.heappop(min_heap)

    return [key for val, key in min_heap]


print(top_frequent_items([1,5,5,2,2,3,5], 2))