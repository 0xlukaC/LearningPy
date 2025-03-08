#!/usr/bin/python3


from typing import KeysView


def enpve(func):
    def wrapper(a):
        if a % 2 == 0:
            return func(a)
        else:
            return None

    return wrapper


@enpve
def test(a):
    print(a)


test(1)
test(2)
print("")


def logs_args(func):
    def wrapper(a1, a2):
        print(f"logged 1 {a1}")
        print(f"logged 2 {a2}")
        return func(a1, a2)

    return wrapper


@logs_args
def tlog(a, b):
    print(f"function {a} {b}")


tlog("hello", "world")

print("")


def keyLogs(func):
    def wrapper(*args, **kwargs):
        print(args)  # tuple
        print(kwargs.items())  # dictionary
        for arg in args:
            print(f"Logged: {arg}")
        for key, value in kwargs.items():
            print(f"Logged {key}: {value}")
        return func(*args, **kwargs)

    return wrapper


@keyLogs
def testKey(*args, **kwargs):
    print(f"function got {args} {kwargs}")


testKey("Hello", "World", key1="value1", key2="value2")
print("")

import time


def bunnis(func):
    def wrapper():
        current_hour = int(time.strftime("%H"))  # 24 hour format
        if 9 <= current_hour < 17:
            return func
        else:
            return None

    return wrapper


@bunnis
def testTime():
    print(f"hour: {hour}")


testTime()
