# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List

# From GPT


def longest_common_prefix(strs: List[str]) -> str:
    prefix = strs[0]

    for substr in strs[1:]:
        while substr[:len(prefix)] != prefix:
            prefix = prefix[:-1]

            if not prefix:
                return ""
    return prefix
