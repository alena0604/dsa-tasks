# 03.02

def compress_str(s):
    number = 1
    s_list = list(s)
    new_list = []

    for i in range(1, len(s_list)):
        if s_list[i] == s_list[i - 1]:
            number += 1
        else:
            new_list.append(s_list[i - 1])
            if number > 1:
                new_list.append(str(number))
    return "".join(new_list)


print(compress_str("hello"))

