#!/usr/bin/python3

import math


def ensureFloat(func):
    def wrapper(n):
        for i in n:
            if type(i) != float:
                return None
        return func(n)

    return wrapper


@ensureFloat
def mean(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)


@ensureFloat
def mode(arr):
    d = {}
    for i in arr:
        if str(i) in d:
            d[str(i)] += 1
        else:
            d[str(i)] = i

    maxN = [0]
    mode_values = []

    for value, count in d.items():
        if count > maxN[0]:
            maxN[0] = count
            mode_values = [value]
        elif count == maxN[0]:
            mode_values.append(value)
    return mode_values


@ensureFloat
def median(arr):
    arr = sorted(arr)
    half = math.floor(len(arr) / 2)
    if len(arr) % 2 == 0:
        return [arr[half - 1], arr[half + 1]]
    return arr[half]
