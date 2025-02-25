#!/usr/bin/python

def add(num1, num2):
    return print(num1 + num2)

def calculate_total(prices, discount=10):
    total = 0
    for x in prices:
        total += x
    return total*((100 - discount)/100)

mylist = [43, 34, 12, 5]

print(calculate_total(mylist, 10))

