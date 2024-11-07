from typing import List


def find_relative_ranks(score: List[int]) -> List[str]:
    str_places = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    score_list = [str(i) for i in range(1, len(score) + 1)]
    if len(score) > 3:
        str_places = str_places + score_list[3:]
    dic_map = {}
    sorted_score = sorted(score, reverse=True)
    for s, p in zip(sorted_score, str_places):
        dic_map[s] = p
    return [dic_map[i] for i in score]


print(find_relative_ranks([10,3,8,9,4]))


def find_relative_ranks_v2(score: List[int]) -> List[str]:
    sorted_score = sorted(enumerate(score), key=lambda x: -x[1])

    result = [""] * len(score)

    for i, (index, _) in enumerate(sorted_score):
        if i == 0:
            result[index] = "Gold Medal"
        elif i == 1:
            result[index] = "Silver Medal"
        elif i == 2:
            result[index] = "Bronze Medal"
        else:
            result[index] = str(i + 1)

    return result
