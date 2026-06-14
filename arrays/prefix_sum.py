def prefix_sum(arr, ind_1, ind_2):
    prefix_sum = []
    sum_el = 0
    for i in range(len(arr)):
        sum_el += arr[i]
        prefix_sum.append(sum_el)
    if ind_1 == 0:
        return prefix_sum[ind_2]
    return prefix_sum[ind_2] - prefix_sum[ind_1-1]


print(prefix_sum([1,2,3,4,5], 0, 3))