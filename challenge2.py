#!/usr/bin/python3


def replace(input):
    replacedString = ""
    for i in range(len(input)):
        if input[i] == " ":
            replacedString += "%20"
        else:
            replacedString += input[i]
    return replacedString


print(replace("Hello World"))
print(replace("Python Programming"))
print(replace("Replace spaces with %20"))

print(replace(input("input: ")))
