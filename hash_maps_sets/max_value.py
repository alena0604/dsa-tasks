# Define a function which takes a dictionary as a parameter and returns the key
# with the highest value in a dictionary.
#
# Example:
#
#     my_dict = {'a': 5, 'b': 9, 'c': 2}
#     max_value_key(my_dict))
# Output:
#
# b


def max_value(my_dict):
    max_value = max(my_dict.values())
    for key in my_dict:
        if my_dict[key] == max_value:
            return key


print(max_value({"a": 5, "b": 9, "c": 2}))


def max_value_efficient(my_dict):
    return max(my_dict, key=my_dict.get)


print(max_value_efficient({"a": 5, "b": 9, "c": 2}))
