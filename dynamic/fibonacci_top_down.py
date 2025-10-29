def fib_memory(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fib_memory(n-1, memo) + fib_memory(n-2, memo)
    return memo[n]


fib_dict = {}
print(fib_memory(7, fib_dict))