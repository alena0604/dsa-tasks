# Find the index of the first non-repeating character in a string.
# Build a frequency map, then do a second pass to return the first character with count 1.
# input = "hello" output = l
from collections import Counter


def first_unique_char(word):
    frequency = Counter(word)
    for key, val in enumerate(word):
        if frequency[val] == 1:
            return val
    return -1

print(first_unique_char("aashaneo"))