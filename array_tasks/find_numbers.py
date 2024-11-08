# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.


from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    all_numbers = set(range(1, len(nums) + 1))
    nums_set = set(nums)
    return list(all_numbers - nums_set)


print(find_disappeared_numbers([1, 1]))
