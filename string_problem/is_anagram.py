from collections import Counter


# Time O(n+m)
# Space O(n+m) - due to lower
def is_anagram(str1, str2):
    return Counter(str1.lower()) == Counter(str2.lower())


print(is_anagram("weerte", "Ertewe"))
