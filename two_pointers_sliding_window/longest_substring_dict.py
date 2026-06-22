def longest_unique_substr(s: str):
    left = 0
    max_len = 0
    seen = {}
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len


print(longest_unique_substr("pwwkew"))