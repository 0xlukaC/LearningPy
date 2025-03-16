#!/usr/bin/python3

import math
import random
import time


def calc(n):
    return print(
        f"n is sqrt: {math.sqrt(n)}, factorial: {math.factorial(n)}, {math.pow(n, 2)}"
    )


def dice():
    return print(random.randint(1, 6))


def looptime():
    tic = time.perf_counter()  # Start Time
    for _ in range(1000000):
        ...
    toc = time.perf_counter()  # End Time
    return print(f"Build finished in {toc - tic:0.4f} seconds")


def timer(n):
    time.sleep(n)
    print("times up")


calc(3)
dice()
looptime()
timer(4)
