def longest_substr(s: str):
    left = 0
    max_len = 0
    char_index = {}
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1     # jump 
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

print(longest_substr("abcddef"))
