import heapq


def nlargest(arr, k):
    heap = []
    for item in arr:
        heapq.heappush(heap, item)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap


print(nlargest([3, 5, 1, 2, 11], 3))