from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    result_index = [-1, -1]

    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            print(nums[mid])
            result_index[0] = mid
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result_index[1] = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result_index


print(search_range([5,7,7,8,8,10], 8))