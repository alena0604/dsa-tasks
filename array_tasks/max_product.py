# Given an integer arr, return the max product of any three numbers in the array

def max_product(max_prod_arr):
    max_prod_arr.sort()
    return max_prod_arr[-1]*max_prod_arr[-2]*max_prod_arr[-3]