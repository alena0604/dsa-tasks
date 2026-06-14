# compress string
# input = "aabbbccdeeee"
# output = a2b3c2d1e4

def compress_str(s):
    result = []
    i = 0
    while i < len(s):
        ch = s[i]
        count = 0
        while i < len(s) and s[i] == ch:
            count += 1
            i += 1
        result.append(ch)
        result.append(str(count))
    return "".join(result)

print(compress_str("aabbbccdeeee"))
