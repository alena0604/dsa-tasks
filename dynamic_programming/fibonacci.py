
# Bottom Up with Memorisation

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


# Top Down with tabulation

def fib_tab(n):
    tb = [0,1]
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])
    return tb[n-1]

print(fib_tab(9))