#!/usr/bin/python3

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Constant O(1)
c = arr[1]

# Linear O(n)
for _ in arr:
    ...

# Quadratic O(n^2)
for _ in arr:
    for _ in arr:
        ...
