# You are given two strings s and t such that every character occurs at most
# once in s and t is a permutation of s.
# The permutation difference between s and t is defined as the sum of the absolute difference
# between the index of the occurrence of each character in s and the index of the occurrence of the same character in t.
# Return the permutation difference between s and t.


def find_permutation_difference(s: str, t: str) -> int:
    s_list = list(s)
    t_list = list(t)

    result = [abs(i - t_list.index(s_list[i])) for i in range(0, len(s_list))]
    return sum(result)


print(find_permutation_difference("abcde", "edbac"))
