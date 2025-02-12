#!/usr/bin/python3


def chess(row, col):
    if row < 1 or row > 8:
        return None
    if col < 1 or col > 8:
        return None
    if row % 2 != 0 or col % 2 != 0:
        return "black"
    return "white"


print(chess(2, 2))
