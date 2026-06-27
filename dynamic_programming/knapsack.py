def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n+1)]     # creating matrix

    for i in range(1, n+1):
        weight = weights[i-1]
        value = values[i-1]

        for j in range(1, capacity+1):
            # skip
            dp[i][j] = dp[i-1][j]

            # take
            if weight <= j:
                dp[i][j] = max([dp[i-1][j], value + dp[i-1][j - weight]])

    return dp[n][capacity]


# For every item:
#
#     Look at every possible backpack size,
#     starting from the biggest:
#
#         Choice 1:
#         Do nothing.
#         Keep my old best answer.
#
#         Choice 2:
#         Put this item in.
#         Add its value to the best smaller backpack.
#
#         Keep whichever is better.

def knapsack_optimised(weights, values, W):
    # dp[c] = best value with backpack capacity c
    dp = [0] * (W + 1)   # [0, 0, 0 , 0 ..] len W + 1

    for w, v in zip(weights, values):   # taking each item

        for c in range(W, w - 1, -1): # go backwards to avoid including item twice
            dp[c] = max(dp[c], v + dp[c - w])   # don't take item, take item

    return dp[W]




weights=[2,3,5]
values=[10,15,25]
capacity=5

print(knapsack_optimised(weights, values, capacity))