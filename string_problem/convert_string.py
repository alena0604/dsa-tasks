# Given two strings word1 and word2, return the minimum number of operations (insert, delete, replace)
# to convert word2 into word1

# s1 = "catch"
# s2 = "carch"
# result = 1

s1 = "table"
s2 = "tbres"
result = 3


def convert_str(s1, s2, index1, index2):  # O(3ⁿ)
    # base case
    # if we reach the end of s1, but s2 still has char, we must insert all char from s2
    if index1 == len(s1):
        return len(s2) - index2
    # If we reach the end of s2, but s1 still has characters left, we must delete all remaining characters from s1.
    if index2 == len(s2):
        return len(s1) - index1
    # If both characters are the same, just move forward without any operation.
    if s1[index1] == s2[index2]:
        return convert_str(s1, s2, index1 + 1, index2 + 1)

    else:
        # Move index2 forward (index1 stays)
        delet_op = 1 + convert_str(s1, s2, index1, index2 + 1)
        # Move index1 forward (index2 stays)
        insert_op = 1 + convert_str(s1, s2, index1 + 1, index2)
        # Move both index1 and index2 forward
        replace_op = 1 + convert_str(s1, s2, index1 + 1, index2 + 1)
        return min(delet_op, insert_op, replace_op)


print(convert_str(s1, s2, 0, 0))
