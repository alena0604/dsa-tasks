def hash_search(arr, target):
    s = set(arr)
    return target in s


print(hash_search([2,5,3,7,4,5], 5))

- Time: **O(1)** on average
- Space: **O(n)**.
