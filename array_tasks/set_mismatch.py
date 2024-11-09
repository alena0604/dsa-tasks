from typing import List


# should be improved
def find_error_nums(nums: List[int]) -> List[int]:
    original_nums = set([i for i in range(1, len(nums) + 1)])
    missed_num = list(original_nums - set(nums))
    temp_result = []
    duplicated_num = []
    for i in nums:
        if i in temp_result:
            duplicated_num.append(i)
        else:
            temp_result.append(i)
    return duplicated_num + missed_num


print(find_error_nums([1, 1]))
