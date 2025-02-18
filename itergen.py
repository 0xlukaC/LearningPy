#!/usr/bin/python3

from typing import Iterator


def p10() -> Iterator[int]:
    count = 0

    while count < 50:
        yield count
        count += 10


s10 = (i for i in range(0, 50, 10))

it10 = p10()
print(next(it10))
print(next(it10))

print("")

next(s10)
for v in s10:
    print(v)

print("")
# 2

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

genODD = (i for i in arr if i % 2 != 0)
for i in genODD:
    print(i)

print("")
# Range


def range2(start, stop=None, step=1) -> Iterator[int]:
    if stop == None:
        temp = start
        start = 0
        stop = temp
    i = start
    while (step > 0 and i < stop) or (step < 0 and i > stop):
        yield i
        i += step


# chat gpt test cases
def test_range2():
    print("Test case 1: Only stop parameter")
    for num in range2(5):
        print(num, end=" ")
    print("\nExpected: 0 1 2 3 4\n")

    print("Test case 2: Start and stop parameters")
    for num in range2(2, 5):
        print(num, end=" ")
    print("\nExpected: 2 3 4\n")

    print("Test case 3: Start, stop, and step parameters")
    for num in range2(2, 10, 2):
        print(num, end=" ")
    print("\nExpected: 2 4 6 8\n")

    print("Test case 4: Negative step")
    for num in range2(5, 0, -1):
        print(num, end=" ")
    print("\nExpected: 5 4 3 2 1\n")

    print("Test case 5: Negative step with start and stop")
    for num in range2(10, 2, -2):
        print(num, end=" ")
    print("\nExpected: 10 8 6 4\n")


test_range2()
