# Kth Largest Element in a Stream
# Maintain a min-heap of size k for continuous updates.

import heapq

class KthLargest:
    def __init__(self, nums, k):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add_value(self, value):
        heapq.heappush(self.min_heap, value)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap

kth = KthLargest([2,3,4,5], 3)
print(kth.add_value(2))
print(kth.add_value(8))