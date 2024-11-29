# check if two lists are permutations


def check_permute(list_one, list_two):
    if len(list_one) != len(list_two):
        return "not permutation"
    permute_list = []
    for i in list_one:
        if i in list_two:
            permute_list.append(i)
    if len(set(permute_list)) == len(set(list_two)) and len(set(permute_list)) == len(
        set(list_one)
    ):
        return "permutation"
    else:
        return "not permutation"


print(check_permute(["r", "w", "w"], ["w", "r", "s"]))


def num_permutation(list_one, list_two):
    if len(list_one) != len(list_two):
        return "not permutation"
    list_one.sort()
    list_two.sort()
    if list_one == list_two:
        return "permutation"
    else:
        return "not permutation"
