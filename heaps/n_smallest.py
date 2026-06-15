import heapq


def n_smallest(arr, k):
    heap = []
    for val in arr:
        heapq.heappush(heap, -val)
        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0]

print(n_smallest([3, 5, 1, 2, 11], 2))