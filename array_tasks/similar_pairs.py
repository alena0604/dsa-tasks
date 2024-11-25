# You are given a 0-indexed string array words.
#
# Two strings are similar if they consist of the same characters.
#
# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and
# the two strings words[i] and words[j] are similar.


from typing import List


def similar_pairs(words: List[str]) -> int:
    count_result = 0

    seen_set = {}
    for word in words:
        frozen_s = frozenset(word)  # Convert to frozenset for unordered uniqueness
        if frozen_s in seen_set:
            count_result += seen_set[frozen_s]  # Increment count for all previous occurrences
            seen_set[frozen_s] += 1  # Update the count of this set
        else:
            seen_set[frozen_s] = 1
    return count_result


print(similar_pairs(["aabb","ab","ba"]))