# Problem: Find the length of the longest substring without repeating characters.
# Recognition: Finding unique substrings → Likely Sliding Window.

s = "abcabcbb"
output = "abc"


def longest_substr(s):
    set_substr = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while right in set_substr:
            set_substr.remove(s[left])
            left += 1

        set_substr.add(s[right])
        max_length = max(max_length, right - left + 1)
