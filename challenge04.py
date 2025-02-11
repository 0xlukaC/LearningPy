#!/usr/bin/python3


def createtable():
    return [f"{i}: {chr(i)} " for i in range(32, 126)]


print("".join(createtable()))
