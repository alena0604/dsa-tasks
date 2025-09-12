def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [2,3,1,5,9,6]
print(selection_sort(arr))


# O(n^2)
# Space O(1)
# - space efficient
# - easy to implement
# - time is not efficient