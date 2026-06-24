# A robot starts top-left in an m×n grid, can only move right or down.
# How many unique paths to bottom-right?

# To reach (i,j), the robot came from above (i-1,j) or from the left (i,j-1).
# So: paths(i,j) = paths(i-1,j) + paths(i,j-1).


def unique_paths(m, n):     # Input: m and n: the number of rows and columns in the grid.
    dp = [[1]*n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]


print(unique_paths(2, 4))