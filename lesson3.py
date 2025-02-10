#!/usr/bin/python3


def forLoop():
    for i in range(1, 20):
        print(i)


def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    return str(i)


def betterFizzBuzz(i):
    return print((("Fizz" * (not i % 3)) + ("Buzz" * (not i % 5))) or str(i))


# forLoop()
betterFizzBuzz(3)  # Fizz
betterFizzBuzz(5)  # Buzz
betterFizzBuzz(15)  # FizzBuzz
betterFizzBuzz(7)  # 7
