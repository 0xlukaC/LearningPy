#!/usr/bin/python3


def twoInputs(num1, num2):
    print(num1 + num2, num1 - num2, num1 * num2, num1 / num2)


def askUser(name, age, favColor):
    print(
        f"{name + ('\'' if name.endswith('s') else '\'s')} age is {age} and their favorite color is {favColor}"
    )


def temp(temperature, mesurement):
    try:
        temperature = float(temperature)
        if mesurement == "c":
            print(f"{temperature * 1.8 + 32:.2f}")
        elif mesurement == "f":
            print(f"{(temperature - 32) * (5 / 9):.2f}")
    except ValueError:
        print("invalid")


# twoInputs(2, 3)
# askUser(input("name "), input("age "), input("colour "))
temp(input("convert temperature: "), input("from (c/f): "))
