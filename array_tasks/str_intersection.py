def find_the_difference(s: str, t: str) -> str:
    for i in t:
        if i not in s:
            return i
        else:
            s = s.replace(i, "", 1)
    return ""


print(find_the_difference(s = "a", t = "aa"))