# Duplicate Number

# Write a function to remove the duplicate numbers on given integer array/list.

# Example
#
#     remove_duplicates([1, 1, 2, 2, 3, 4, 5])
#     Output : [1, 2, 3, 4, 5]


def remove_duplicate(dup_list):
    return list(set(dup_list))


dup_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicate(dup_list))
