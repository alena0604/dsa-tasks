def pair_sum(nums, target): # O(n)
    temp_val = {}

    for i, v in enumerate(nums):
        complement = target - v

        if complement in temp_val:
            return temp_val[complement], i

        print(temp_val)
        temp_val[v] = i
    return []

print(pair_sum([1, 2, 1, 4, 5], 5))