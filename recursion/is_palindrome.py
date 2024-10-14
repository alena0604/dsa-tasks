

def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True

    # Check if the first and last characters are the same, and call recursively for the substring
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


print(is_palindrome("tacocat"))


# Comparing the first and last characters:

# s[0] refers to the first character of the string.
# s[-1] refers to the last character of the string.

# is_palindrome("racecar")
# is_palindrome("aceca")
# is_palindrome("cec")
# is_palindrome("e")