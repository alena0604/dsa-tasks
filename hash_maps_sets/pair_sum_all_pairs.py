# Pairs
#
# Write a function to find all pairs of an integer
# array whose sum is equal to a given number.
# Do not consider commutative pairs.


def pair_sum(pair_list, pair_sum):
    for i in pair_list:
        var_sub = pair_sum - i
        if var_sub in pair_list and var_sub != i:
            print(i, var_sub)


pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)


def pair_sum_again(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result
