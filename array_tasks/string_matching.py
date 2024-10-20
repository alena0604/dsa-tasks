# Given an array of string words,
# return all strings in words that is a substring of another word.
# You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

from typing import List


def string_matching(words: List[str]) -> List[str]:
    new_list = []
    for word in words:
        for j in words:
            if j in word and j != word:
                print(j, word)
                new_list.append(j)
    return list(set(new_list))


print(string_matching(["ga", "ugao", "dbh", "a"]))
