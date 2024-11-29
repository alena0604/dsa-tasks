# from GPT
def flatten(arr):
    result = []

    for element in arr:
        if isinstance(element, list):
            # If the element is a list, recursively flatten it and extend the result
            result.extend(flatten(element))
        else:
            # If the element is not a list, append it to the result
            result.append(element)

    return result
