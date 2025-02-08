# Given a string s and a set of words wordDict,
# determine if s can be segmented into a sequence of one or more dict words

s = "applepenapple"
word_list = ["apple", "pen"]


def find_sequence(s, word_list):
    word_set = set(word_list)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


print(find_sequence(s, word_list))
