# Given an integer array nums and an integer k,
# return the number of pairs (i, j) where i < j such
# that |nums[i] - nums[j]| == k.
from typing import List


def count_k_difference(nums: List[int], k: int) -> int:
    result = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                result += 1
    return result


print(count_k_difference([1, 2, 2, 1], 1))


from collections import Counter


def count_k_diff(nums: List[int], k: int) -> int:
    counter = Counter(nums)
    result = 0

    for num in counter:
        result += counter[num] * counter.get(num + k, 0)

    return result


print("Efficient", count_k_diff([1, 2, 2, 1], 1))
