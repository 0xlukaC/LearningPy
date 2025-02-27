#!/usr/bin/python3


def createtable():
    return [f"{i}: {chr(i)} " for i in range(32, 126)]


# print("".join(createtable()))

f = "".join(["1", "2", "3"])  # joins without spaces
print(f)
