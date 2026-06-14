# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
#
# A common string with the least index sum is a common string such that if
# it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
#
# Return all the common strings with the least index sum. Return the answer in any order.


from typing import List


def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
    common = dict()
    for word in list1:
        if word in list2:
            common[word] = list1.index(word) + list2.index(word)
    min_sum = min(common.values())
    return [key for key, value in common.items() if value == min_sum]


print(
    find_restaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
    )
)
