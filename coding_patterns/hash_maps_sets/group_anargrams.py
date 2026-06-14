# Cluster strings that are anagrams of each other.
# Sort each word alphabetically to get a canonical key, then bucket words by that key in a hashmap.
# input = ["eat","tan","bat","nat","tea","ate"]
# output = [[eat,tea,ate],[tan,nat],[bat]]
from collections import defaultdict


def group_anagrams(arr):
    groups = defaultdict(list)
    for word in arr:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return groups.values()

print(group_anagrams(["eat","tan","bat","nat","tea","ate"]))