#!/usr/bin/python3


# O(n)
def replace(input):
    replacedString = []

    for i in input:
        if i == " ":
            replacedString.append("%20")  # append doesnt create a new array
        else:
            replacedString.append(i)
    return "".join(replacedString)


print(replace("Hello World"))
print(replace("Python Programming"))
print(replace("Replace spaces with %20"))

# print(replace(input("input: ")))
