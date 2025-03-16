#!/usr/bin/python3

import sd_maintain as maths

arr = [1.5, 2.5, 3.0, 1.5, 2.5, 2.5]
print(maths.median(arr))  # Output: 3

arr = [1.5, 2.5, 3.0, 1.5, 2.5, 2.5]
print(maths.mode(arr))

arr = [1.5, 2.5, 3.0, 1.5, 2.5, 2.5]
print(maths.mean(arr))


# refactor
def print_details(role, name, age, department):
    print(f"{role} Name: {name}")
    print(f"{role} Age: {age}")
    print(f"{role} Department: {department}")


print_details("Employee", "Alice", 30, "HR")
print_details("Manager", "Bob", 40, "Finance")
