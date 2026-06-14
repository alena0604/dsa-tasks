# Return all elements that appear more than once.
# Use a frequency hashmap — on the second occurrence, add the element to the result list.
# input = [4, 3, 2, 7, 8, 2, 9, 3]
# output = [2, 3]
from collections import Counter


def find_duplicates(arr):
    frequency = Counter(arr)
    return [key for key, val in frequency.items() if val > 1]

print(find_duplicates([4, 3, 2, 7, 8, 2, 9, 3]))
