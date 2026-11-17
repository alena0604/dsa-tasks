# merge intervals

def merge_intervals(busy):
    result = []
    for start, end in busy:
        if result and start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)     # in results are previous intervals, compare with a new
        else:
            result.append([start, end])

    return result


def find_free_slots(busy, day=(0, 24)):
    merged = merge_intervals(busy)
    free = []
    current = day[0]

    for start, end in merged:
        if start > current:
            free.append([current, end])

        current = max(current, end)

    if current < day[1]:
        free.append([current, day[1]])

    return free

busy = [
    [1, 3],
    [2, 6],
    [8, 10],
    [6, 7]
]

print(merge_intervals(busy))
print(find_free_slots(busy, (0, 18)))