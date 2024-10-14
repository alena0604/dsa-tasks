from typing import List


def prefixCount(words: List[str], pref: str) -> int:
    prefix_lens = len(pref)
    count_w = 0
    for w in words:
        if w[:prefix_lens] == pref:
            count_w += 1

    return count_w



print(prefixCount(["pay","attention","practice","attend"], "at"))