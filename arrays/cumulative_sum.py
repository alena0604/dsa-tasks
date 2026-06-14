# determine the maximum cumulative sum within a sequence of numbers


seq = [4, -1, 2, 1, -5, 4]
result = 6


def cumulative_sum(seq) -> int:
    curr_sum = 0
    max_sum = float("-inf")

    for num in seq:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum
