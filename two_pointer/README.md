1. How to Recognize a Two Pointers Problem
✅ The problem involves a sorted array or linked list.
✅ You need to find a pair or subset that satisfies a condition (e.g., sum, difference, partition).
✅ You can solve the problem using O(N) instead of O(N²) by eliminating unnecessary comparisons.
✅ You are dealing with merging two sorted arrays or checking overlapping intervals.

2. General Solution Structure
Whenever you spot a two-pointers problem, follow these steps:

Step 1: Identify the movement strategy
Opposite ends? → Move toward the center (e.g., two sum, palindrome check).
Same direction? → One pointer scans while the other updates (e.g., removing duplicates, merging).

Step 2: Initialize pointers
Left and right at the ends for opposite ends problems.
One pointer slower than the other for in-place modifications.

Step 3: Define the stopping condition
Until left < right for opposite-end problems.
Until one list is exhausted for merging problems.

Step 4: Move pointers based on conditions
Adjust pointers dynamically based on the required condition (e.g., sum, equality, next unique element).
