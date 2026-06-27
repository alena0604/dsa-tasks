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


weights=[2,3,5]
values=[10,15,25]
capacity=5

print(knapsack(weights, values, capacity))