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

[s8161133@dt11 work]$ vim lists.py
[s8161133@dt11 work]$ vim lists.py
[s8161133@dt11 work]$ vim lists.py
[s8161133@dt11 work]$ cat lists.py
#!/usr/bin/python

mylist = ['h', 'e', 'l', 2, 'o']
print(mylist[len(mylist) - 1])


oneto20 = [i + 1 for i in range(20)]

ten = [i + 1 for i in range(10)]
ten.remove(2)
ten.pop(5) # pop is indexed

squares = [i ** 2 for i in range(50) if i > 20]

Nested = [[79, 4, 36], [67, 98, 44, 12, 26], [50], [32, 96, 15, 24, 46], [5, 74, 99, 50, 42, 34, 28], [37], [72, 60, 26], [79, 3, 25, 95, 19, 17], [98, 19], [99, 77, 94, 40, 44, 76, 17, 72, 56]]

newList = [len(i) for i in Nested]

print(newList)
