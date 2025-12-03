def compress_str(s):
    count = 1
    result = []

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1

    result.append(s[-1] + str(count))
    return "".join(result)


print(compress_str("hello"))