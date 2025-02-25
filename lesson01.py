#!/usr/bin/python

a = 3

print(a)
a = float(3) #cast
print(a)
print(type(a))

A = 5

print(A + a) # prints a float due to type promotion

b = a // A # divides then floors it
b = a ** A # exponential
print(b)

s = "hello"
t = "world"

print(s + t)
print(s, t)
print(f"{s} + {t}") # templates
print(s * 3) # prints 3 times (needs to be an int)

print(s[1])
print(s[1:4]) # slice
x = slice(1, 4)
print(a[x]) # also works


def foo(x, y):
    return x + y;

def bar():
    print("hello")

def foobar(name1, name2="Luka") # fallback (like in bash) look up keyword arguments
    print(name1, name2)

foobar("gorg")
foobar("luka2")

def funcc(*names):
    print(names)

funcc("name1", "name2", "name3", "name4")

def addTri(num1, num2):
    return (num1 + num2) * 3

addTri(2, 3)

lambdaAdd = lambda a, b: 3*(a+b) # anonymous function (assigns to var like in js). Can also pass other functions
print(lambdaAdd(3, 4))

numbers = [1, 2, 3] # list not array

# map(lambda, numbers) # function, iterable 

result = list(map(lambda n: n**2+2, numbers))
print(result)




















