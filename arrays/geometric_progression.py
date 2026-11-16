from collections import defaultdict


def find_tripplets_geometric_progression(arr):
    tripplets = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j + 1, len(arr)):

                if arr[j] * arr[j] == arr[i] * arr[k]:
                    tripplets.append((arr[i], arr[j], arr[k]))
                else:
                    continue
    return len(tripplets)


def hash_tripplets_geometric_progression(arr):
    left_map = defaultdict(int)
    triplets = 0

    for i in range(len(arr)):   # middle
        for j in range(i+1, len(arr)):      # right
            if arr[i] * arr[i] % arr[j] == 0:
                left = arr[i] * arr[i] // arr[j]
                if left in left_map:
                    triplets += left_map[left]
        left_map[arr[i]] += 1
    return triplets


def ratio_tripplets_geometric_progression(arr, r):
    second = defaultdict(int)
    third = defaultdict(int)
    triplets = 0

    for x in arr:
        triplets += third[x]
        third[x * r] += second[x]
        second[x * r] += 1

    return triplets


def find_pairs_geometric_progression(arr):
    pairs = []
    ratio = None

    for i in range(len(arr) - 1):
        curr_ratio = arr[i + 1] / arr[i]
        if ratio is None:
            ratio = curr_ratio
        elif curr_ratio != ratio:
            return False
        pairs.append((i, i + 1))
    return pairs


print(ratio_tripplets_geometric_progression([1, 2, 2, 4], 2))
