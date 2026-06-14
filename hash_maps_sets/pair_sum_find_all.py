# Write a program to find all pairs of integers whose sum is equal to a given number


def find_pair(arr, sum):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                return arr[i], arr[j]


# from leetcode


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [complement, num]

        seen[num] = i


# print(two_sum([2, 6, 3, 9, 11], 9))


# two pointer method
def two_sum_sorted(arr, target):
    # Initialize two pointers
    arr.sort()
    left = 0
    right = len(arr) - 1

    # Loop until the pointers meet
    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return arr[left], arr[right]  # Return the pair if sum matches the target

        elif current_sum < target:
            left += 1  # Move the left pointer to the right to increase the sum

        else:
            right -= 1  # Move the right pointer to the left to decrease the sum

    return None


# print(two_sum_sorted([2, 6, 3, 9, 11, 1, 8], 9))
