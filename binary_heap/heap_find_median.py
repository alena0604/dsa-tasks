import heapq


class MedianValue():
    def __init__(self):
        self.low = []
        self.high = []

    def add_value(self, value):
        heapq.heappush(self.low, -value)

        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0])/2


mfv = MedianValue()
mfv.add_value(1)
mfv.add_value(5)
mfv.add_value(2)
mfv.add_value(3)

print(mfv.low, mfv.high, mfv.find_median())