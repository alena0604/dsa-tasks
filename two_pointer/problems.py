# Example 1: Two Sum (Sorted Array)
# Problem: Find two numbers in a sorted array that add up to a given target.

arr = [1, 2, 3, 4, 6]
target = 6


def two_sum(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return []


def two_sum_dict(arr, target):
    temp_list = {}

    for i, num in enumerate(arr):
        sub_num = target - num
        if sub_num in temp_list:
            return num, sub_num
        temp_list[num] = i

    return []


# remove duplicates
# Problem: Remove duplicates from a sorted array in-place so that each element appears only once.
# slow pointer and fast pointer, moving the same direction

input = [1, 1, 2, 2, 3, 4]
output = [1, 2, 3, 4]


def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:  # if elements are the same only fast is moving!
            slow += 1
            nums[slow] = nums[fast]
    return nums[: slow + 1]


# Problem: Given two sorted arrays, merge them into one sorted array without extra space.
