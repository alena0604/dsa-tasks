# x^n = x * x^(n-1)


def power_num(x, n):
    assert int(n) == n, "The number should be integer"
    if n == 0:
        return 1
    elif n < 0:
        return 1/x * power_num(x, n+1)
    else:
        return x * power_num(x, (n-1))


print(power_num(2, 4))


# explanation:

# power_num(2, 3)
# = 2 * power_num(2, 2)
# = 2 * (2 * power_num(2, 1))
# = 2 * (2 * (2 * power_num(2, 0)))
# = 2 * (2 * (2 * 1))  # Base case reached when n == 0
# = 8


# power_num(2, -2)
# = 1/2 * power_num(2, -1)
# = 1/2 * (1/2 * power_num(2, 0))
# = 1/2 * (1/2 * 1)  # Base case reached when n == 0
# = 0.25
