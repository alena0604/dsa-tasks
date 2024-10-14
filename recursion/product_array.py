def product_array(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_array(arr[1:])


print(product_array([1, 2, 3, 10]))


# First call: productOfArray([1, 2, 3, 4]) → 1 * productOfArray([2, 3, 4])
# Second call: productOfArray([2, 3, 4]) → 2 * productOfArray([3, 4])
# Third call: productOfArray([3, 4]) → 3 * productOfArray([4])
# Fourth call: productOfArray([4]) → 4 * productOfArray([])
# Base case: productOfArray([]) → returns 1
