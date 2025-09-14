def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1     # starting from -1 point where there is no elements 
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1      # start the sorting index 
            arr[i], arr[j] = arr[j], arr[i]     # swap elements that are smeller than pivot
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low < high:          # condition ensures recursion stops
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)    # sort left side
        quick_sort(arr, pi + 1, high)     # sort right side


arr = [2, 4, 7, 10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


# O(n log n) average, O(n²) worst