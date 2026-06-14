# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in any order.


from itertools import combinations


def subsets(nums):
    result = []
    for i in range(len(nums) + 1):
        result.extend(combinations(nums, i))
        print(result)
    return [list(subset) for subset in result]


print(subsets([1, 2, 3]))
