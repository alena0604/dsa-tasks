# 1. Given two arrays, write a function to get the intersection of the two.
# 2. Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and
# you may return the result in any order.
from typing import List
from collections import Counter


def intersection(arr_one, arr_two):
    return [i for i in arr_one if i in arr_two]


print(intersection([1, 2, 3, 4, 5], [0, 1, 3, 7]))


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    counter = Counter(nums1)
    intersection = []

    for i in nums2:
        if counter[i] > 0:
            intersection.append(i)
            counter[i] -= 1
    return intersection



