def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])


print(length_of_last_word("luffy is still joyboy"))