from collections import defaultdict


def subarray_sum(arr, k):
    count = defaultdict(int)
    count[0] = 1
    total = 0
    res = 0

    for n in arr:
        total += n
        res += count[total - k]
        count[total] += 1

    return res


print(subarray_sum([1, 2, 3, 2, 2, 1, 1, 1], 3))