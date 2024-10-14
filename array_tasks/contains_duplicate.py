# Contains Duplicate

# Given an integer array nums, return true
# if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(dup_list):
    return len(dup_list) != len(set(dup_list))


nums = [1,2,3,1]
print(contains_duplicate(nums))
