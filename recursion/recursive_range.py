# Write a function called recursiveRange which accepts a number
# and adds up all the numbers from 0 to the number passed to the function.


def recursive_range(n):
    assert n >= 0 and int(n) == n, "The number should be positive"
    if n == 0:
        return 0
    if n == 1:  # don't need this case
        return 1
    return n + recursive_range(n - 1)



print(recursive_range(1))