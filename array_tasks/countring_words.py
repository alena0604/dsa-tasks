from typing import List


def prefix_count(words: List[str], pref: str) -> int:
    prefix_lens = len(pref)
    count_w = 0
    for w in words:
        if w[:prefix_lens] == pref:
            count_w += 1

    return count_w



print(prefix_count(["pay","attention","practice","attend"], "at"))