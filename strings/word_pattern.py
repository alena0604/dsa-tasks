# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between
# a letter in pattern and a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.


def word_pattern(pattern: str, s: str) -> bool:
    s_list = s.split()
    if len(pattern) != len(s_list):
        return False
    pattern_to_word = {}
    word_to_pattern = {}
    for letter, word in zip(pattern, s_list):
        if letter in pattern_to_word.keys():
            if word != pattern_to_word[letter]:
                return False
        else:
            pattern_to_word[letter] = word

        if word in word_to_pattern:
            if word_to_pattern[word] != letter:
                return False
            else:
                word_to_pattern[word] = letter
    return True


print(word_pattern("aaa", "aa aa aa aa"))
