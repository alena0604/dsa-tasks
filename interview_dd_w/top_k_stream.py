import heapq
from collections import defaultdict


class TopKStream:
    def __init__(self, k: int):
        self.k = k
        self.count_orders = defaultdict(int)
        self.heap = []

    def add_item(self, item):
        self.count_orders[item] += 1
        count = self.count_orders[item]
        self.heap = [(count, i) for i, count in self.count_orders.items() if i != item]
        heapq.heapify(self.heap)

        heapq.heappush(self.heap, (count, item))

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def get_top_k(self):
        return [item for _, item in sorted(self.heap, reverse=True)]


top_k = TopKStream(2)

top_k.add_item("apple")
top_k.add_item("banana")
top_k.add_item("apple")
top_k.add_item("orange")
top_k.add_item("banana")
top_k.add_item("apple")

print(top_k.get_top_k())
