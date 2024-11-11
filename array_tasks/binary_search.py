# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If target exists, then return its index.
# Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


from typing import List


def search(nums: List[int], target: int) -> int:
    nums.sort()
    left, right = 0, len(nums) - 1

    while left <= right:
        midl = (right + left) // 2
        if nums[midl] == target:
            return midl
        elif nums[midl] < target:
            left = midl + 1
        else:
            right = midl - 1

    return -1
