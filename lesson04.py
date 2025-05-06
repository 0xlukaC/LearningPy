#!/usr/bin/python

# Lists
def foo():
    ...
def bar():
    ...

l = [1, 2, 3]
l2 = ['a', 'b', 'c'] 
l3 = ['a', 2, ['hi'], foo, bar]

print(l[2])
print(l[0:3])
print(l[-3])

l.append(4)
l.remove(1) # actually removes 1
print(2 in l) # "in" is bool

# list comprehensions
# new list = [expression for item in iterable <optional if condition>
squares = [x**2 for x in range(1, 6)]
print(squares)

