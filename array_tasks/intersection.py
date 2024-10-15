# Given two arrays, write a function to get the intersection of the two.


def intersection(arr_one, arr_two):
    return [i for i in arr_one if i in arr_two]


print(intersection([1, 2, 3, 4, 5], [0, 1, 3, 7]))



