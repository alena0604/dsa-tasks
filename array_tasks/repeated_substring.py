# Given a string s, check if it can be constructed
# by taking a substring of it and appending multiple
# copies of the substring together.


def repeatedSubstringPattern(s: str) -> bool:
    ss = (s + s)[1:-1]
    return s in ss


print(repeatedSubstringPattern("aba"))