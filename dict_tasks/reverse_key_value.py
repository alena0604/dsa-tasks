# Reverse Key-Value Pairs
#
# Define a function which takes as a parameter dictionary and returns a dictionary
# in which reverse the key-value pairs are reversed.
#
# Example:
#
#     my_dict = {'a': 1, 'b': 2, 'c': 3}
#     reverse_dict(my_dict)
#
# Output:
#     {1: 'a', 2: 'b', 3: 'c'}

# {key_expr: value_expr for item in iterable}


def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}


print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))
