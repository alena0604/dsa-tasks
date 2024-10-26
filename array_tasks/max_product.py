# Given an integer arr, return the max product of any three numbers in the array

def max_product(max_prod_arr):
    max_prod_arr.sort()
    return max_prod_arr[-1]*max_prod_arr[-2]*max_prod_arr[-3]


import heapq


def max_three(max_prod_arr):
    largest = heapq.nlargest(3, max_prod_arr)
    smallest = heapq.nsmallest(2, max_prod_arr)

    return max(largest[2]*largest[1]*largest[0], largest[0]*smallest[1]*smallest[0])


def max_product_negative(max_prod_arr):
    prod_result = []
    for i in range(len(max_prod_arr)):
        for j in range(i+1, len(max_prod_arr)):
            for k in range(j+1, len(max_prod_arr)):
                prod = max_prod_arr[i] * max_prod_arr[j] * max_prod_arr[k]
                prod_result.append(prod)

    return max(prod_result)


print(max_product_negative([-2, -4, 5, 3]))
