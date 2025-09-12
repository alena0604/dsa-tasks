def bubble_sort(arr):
    for i in range(len(arr) - 1):       # After n-1 passes, the array is sorted (no need for the last pass, because the last element falls into place automatically).
        for j in range(len(arr) - i - 1):   # After each outer loop (each pass), the last i elements are already sorted and we have -1 because j+1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [2,3,1,5,9,6]
print(bubble_sort(arr))

# O(n^2)