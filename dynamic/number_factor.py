# Given N, find the number of ways to express N as a sum of 1, 3, 4

n = 5
result = [1, 4], [4, 1], [3, 1, 1], [1, 3, 1], [1, 1, 3], [1, 1, 1, 1, 1]


def number_ways(n):
    td = [1, 1, 1, 2]
    for i in range(4, n + 1):
        td.append(td[i - 1] + td[i - 3] + td[i - 4])

    return td[n]


print(number_ways(5))
