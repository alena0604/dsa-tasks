# How to find the sum of digits of a positive integer number using recursion


def sum_digits(n):
    assert n >= 0 and int(n) == n, f"Incorrect value {n}"
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(n // 10)


# Recursive Case: return n % 10 + sum_digits(n // 10).
# The last digit of n is obtained with n % 10, and the rest of the digits
# are passed recursively with n // 10.
# This method breaks the number down digit by digit, summing each one.

# sum_digits(4321)
# = 1 + sum_digits(432)    # n % 10 gives 1
# = 1 + (2 + sum_digits(43))
# = 1 + 2 + (3 + sum_digits(4))
# = 1 + 2 + 3 + (4 + sum_digits(0))
# = 1 + 2 + 3 + 4 + 0
# = 10


print(sum_digits(1312))
