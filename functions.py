#!/usr/bin/python3


def add_sum(num1, num2):
    return print(num1 + num2)


def calculate_total(priceList, discount=10):
    total = 0
    for x in priceList:
        total += x
    return total * (1 - discount / 100)


print(f"{calculate_total([1, 2, 3, 4], 10):.2f}")
