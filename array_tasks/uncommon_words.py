# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.


from typing import List
from collections import Counter


def uncommon_from_sentences(s1: str, s2: str) -> List[str]:
    list_common = s1.split() + s2.split()
    counter = Counter(list_common)
    return [key for key, val in counter.items() if val == 1]


print(uncommon_from_sentences("this apple is sweet", "this apple is sour"))
