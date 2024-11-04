from typing import List
from collections import Counter


def majority_element(nums: List[int]) -> int:
    counter = Counter(nums)
    return max(counter, key=counter.get)


print(majority_element([3, 2, 3]))
