# Problem: Find the longest common subsequence between two strings.
# Recognition: Comparing two strings → Likely Dynamic Programming (DP).

str1 = "abcde"
str2 = "ace"
output = "ace", 3


def lcs_substring(str1, str2):
    m, n = len(str1), len(str2)

    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                curr[j] = prev[j] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])

        prev, curr = curr, prev

    return prev[n - 1]


print(lcs_substring(str1, str2))
