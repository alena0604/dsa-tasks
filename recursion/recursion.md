## property of recursion:
 - performing the same operation with different inputs
 - in every step we try smaller inputs to make the problem smaller
 - base condition is needed to stop the recursions, otherwise infinite loop will occur


## schema:
```commandline
 def recursion_method(params):
     if exit from condition satisfied:
         return some value
     else:
         recursion_method(modified params)
```

## Steps:
 1. Find recursive case
 e.g. n! = n * (n-1)!
 2. Stopping criteria
 3. Unintentional case e.g. -1 or 1.5


- recursion that calls twice time complexity is O(branches^depth)
- depth is n branches - number of functions
