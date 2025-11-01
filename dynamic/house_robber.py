# You are a professional robber 🏴‍☠️ planning to rob houses along a street. Each house has some money stored, but:
#
# You cannot rob two adjacent houses (because the alarm will go off 🚨).
# Find the maximum amount of money you can rob without alerting the police.

nums = [2, 7, 9, 3, 1]
result = 12


def house_robber(nums):
    temp_ar = [0] * (len(nums) + 2)  # Create a storage list
    # planning backward helps us know the best choice before we reach each house.
    for i in range(len(nums) - 1, -1, -1):
        temp_ar[i] = max(
            nums[i] + temp_ar[i + 2], temp_ar[i + 1]
        )  # Decide: Rob or Skip

    return temp_ar[0]  # Return the best answer


print(house_robber(nums))


# Top Down with memory
def house_robber_td(arr, curr_index, temp_dict):
    if curr_index >= len(arr):
        return 0
    else:
        if curr_index not in temp_dict:
            first_case = arr[curr_index] + house_robber_td(arr, curr_index + 2, temp_dict)
            second_case = house_robber_td(arr, curr_index + 1, temp_dict)
            temp_dict[curr_index] = max(first_case, second_case)
        return temp_dict[curr_index]


print(house_robber_td(nums, 0, {}))



