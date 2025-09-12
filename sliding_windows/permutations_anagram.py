from collections import Counter


def permutation_str(s1: str, s2: str):
    window_len = len(s2)

    if len(s1) < window_len:
        return False


    window_count = Counter(s1[:window_len])
    s2_count = Counter(s2)

    if window_count == s2_count:
        return True

    for i in range(window_len, len(s1)):
        window_count[s1[i]] += 1
        window_count[s1[i - window_len]] -= 1
        if window_count[s1[i - window_len]] == 0:
            del window_count[s1[i - window_len]]

        if window_count == s2_count:
            return True
    return False

    


print(permutation_str('abceng', 'cn'))
