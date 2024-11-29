# recursive case:
# f(n) = f(n-1) + f(n-2)


def fibonacci(n):
    assert n >= 0 and int(n) == n, f"Incorrect value {n}"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(8))
