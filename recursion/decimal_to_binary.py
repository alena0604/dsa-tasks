def decimal_binary(n):
    assert int(n) == n, "The number should be integer"
    if n == 0:
        return n
    else:
        return n % 2 + 10 * decimal_binary(n // 2)


print(decimal_binary(10))
