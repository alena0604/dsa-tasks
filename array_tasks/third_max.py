# Given an integer array nums, return the third distinct maximum number in this array.
# If the third maximum does not exist, return the maximum number.


from typing import List


def third_max(nums: List[int]) -> int:
    nums_set = list(set(nums))
    nums_set.sort(reverse=True)
    if len(nums_set) < 3:
        return nums_set[0]
    else:
        return nums_set[2]


print(third_max([3, 2, 1]))
