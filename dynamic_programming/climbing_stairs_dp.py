# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many ways can you climb to the top?

n = 4
result = [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]


def climb_stairs(n):
    td = [1, 1, 2]
    for i in range(3, n + 1):
        td.append(td[i - 1] + td[i - 2])
    return td[n]


print(climb_stairs(4))
