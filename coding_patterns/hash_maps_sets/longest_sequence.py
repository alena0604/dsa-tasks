# Find the length of the longest run of consecutive integers. Store all numbers in a set,
# then for each sequence start (no n−1 in set), expand and count forward.
# input = [100, 3, 2, 200, 1, 4]
# output = 4   [1, 2, 3, 4]

def longest_sequence(arr):
    sequence = set(arr)
    best = 0
    for item in sequence:
        if item - 1 not in sequence:
            length = 1
            current = item
            while current + 1 in sequence:
                current += 1
                length += 1

            best = max(best, length)

    return best


print(longest_sequence([100, 3, 2, 200, 1, 4]))
