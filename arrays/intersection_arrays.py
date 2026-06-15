from collections import Counter


def intersection(nums1, nums2):
    nums_dict = Counter(nums1)
    result = []
    for num in nums2:
        if nums_dict[num] > 0:
            nums_dict[num] -= 1
            result.append(num)

    return result

print(intersection([2, 7, 7, 9, 3, 1], [2, 2, 7]))
